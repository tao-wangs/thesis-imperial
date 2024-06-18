import numpy as np
from BayesianAttackGraph import *
import time 


def Compute_Probabilities(BAG):
    # print(f'I HAVE BEEN CALLED')
    # print(f'hello {BAG}')
    MRF = ToMarkov(BAG)
    FG = CreateFactorGraph(MRF)
    t = RunLBP(FG)
    
    return t


def Update_Children_Subnetworks(i, marginals, SN, DAG, replica_mapping):
    # Replicas should be (parent sn_index, parent_node_index) -> (child sn_index, child_node_index)    
    # Replicas should be (parent -> child mappings)
    # parent i -> [(parent's node j, child k, child's node k)]

    # CPD FORMAT
            #      PARENT
            #       T   F
        # CHILD  T  p   q
            #    F 1-p 1-q

    for parent, parent_node, child, child_node in replica_mapping:
        if parent == i:
            pa_prior = marginals[parent_node]
            # Replace the cpd with the new one 
            cpd = SN[child].get_cpds([child_node])
            cpd[0, 0] = pa_prior 
            cpd[1, 0] = 1 - pa_prior
            SN[child].add_cpds(cpd)
            

def CompositionalAnalysis(SN, DAG, replica_mapping=None):
    number_of_subnets = len(SN)
    analysis_enabled = np.zeros(number_of_subnets, dtype=bool)
    analysis_computed = np.zeros(number_of_subnets, dtype=bool)
    # parent_subnetworks_computed = np.zeros(number_of_subnets, dtype=bool)

    # Initialise the root nodes to be analysed

    for i in range(number_of_subnets):
        # If there is no connection to the DAG, then it is initially ready for analysis
        analysis_enabled[i] = np.sum(DAG[:, i]) == 0 

    # Analysis for everything 
    while not np.all(analysis_computed):
        for i in range(number_of_subnets):
            # Grab its parents 
            parent_indices = np.where(DAG[:, i])[0]
            # Check if all parents have been computed
            analysis_enabled[i] = np.all(analysis_computed[parent_indices])
            if analysis_enabled[i] and not analysis_computed[i]:
                marginals = Compute_Probabilities(SN[i])
                analysis_computed[i] = True
                # Update_Children_Subnetworks(i, marginal, SN, DAG, replica_mapping)


def ParallelCompositionalAnalysis(SN, DAG, num_iterations):
    number_of_subnets = len(SN)

    streams = [torch.cuda.Stream() for _ in range(number_of_subnets)]
    computed_events = [torch.cuda.Event() for _ in range(number_of_subnets)]

    for i in range(number_of_subnets - 1, -1, -1):
        # Select the stream for this subnet
        s = streams[i]
        # Operations for this subnet will be enqueued in the selected stream
        with torch.cuda.stream(s):
            # Wait for parent subnets to complete
            parent_indices = np.where(DAG[:, i])[0].tolist()
            for idx in parent_indices:
                # Ensure this stream waits for the completion of parents
                s.wait_event(computed_events[idx])
                
            s.synchronize()
            # Perform the subnet analysis
            BAG = SN[i]                   
            MRF = ToMarkov(BAG)
            FG = CreateFactorGraph(MRF) 
            RunLBP(FG, num_iterations=num_iterations, MAP=True)
            computed_events[i].record()
    
    for s in streams:
        s.synchronize()


# SN is an array of BAGs models for each subnetwork
# analysis_enabled = Boolean array for each subnetwork 
# analysis_computed = Boolean array for each subnetwork
# parent_subnetworks_computed = False * np.array(number_of_subnets)

# Subnetworks 1, 2, 3, 4, 5 
# Subnetwork 2 has parents 1 
# Subnetwork 3 has parents 1 and 2 
# Subnetwork 4 has parents 1


def GenerateGraph(SN, N, max_pa):
    '''
    params:

    SN = number of subnets 
    N = nodes per subnet 
    '''
    # High level representation 
    DAG = GenerateHighLevelRepresentation(SN, N_edges=3)
    BAGS = GenerateSubnetworks(SN, N, max_edges=max_pa)
    # replica_mapping = [] 

    # src, tgt = np.where(DAG > 0)
    # for s, t in zip(src, tgt):
        # pa_idx = np.random.randint(N)
        # ch_idx = np.random.randint(N)
        # Grab the replica and add the connection and the replica CPD 
        # pa_cpd = BAGS[s].get_cpds(pa_idx)
        # BAGS[t].add_node(f'SN_{s}_N0', ch_idx)
        # BAGS[t].add_cpds(pa_cpd)
        # replica_mapping.append((s, pa_idx, t, ch_idx))

    # return BAGS, DAG, replica_mapping
    return BAGS, DAG

    # For each subnetwork we also need to add the information about the attack paths that can be used by
    # the attacker to escalate privileges to that subnetwork. Thus, we need to add one node for each attack path
    
    # from other (parent) subnetworks. These nodes are replicas of the parent nodes that enable an attack path 
    # across subnetworks in the original BAG.
    
    
def GenerateHighLevelRepresentation(SN, N_edges):
    """
    Generates a high level representation of a synthetic AG
    with random connections according to specification.

    Inputs:
        SN -- The number of subnetworks in the network.
        N_edges -- The number of inter-subnetwork edges in the network

    Outputs:
        W -- The connectivity matrix for the high level representation.
    """

    # # Initialise weight and matrix for the network 
    # DAG = np.zeros((SN, SN))

    # # Generate all possible edges to sample from 
    # all_edges = []
    # for i in range(SN):
    #     for j in range(SN):
    #         if i == j:
    #             continue
    #         all_edges.append((i, j))

    # # Uniformly sample N_edges connections 
    # idxs = np.random.choice(len(all_edges), size=N_edges, replace=False)
    # edges = [all_edges[idx] for idx in idxs]
    
    # # Maximum number of parent nodes for each node. 

    # # Set connection weight to be 1 for randomly generated connections
    # # Set random delays for these connections simultaneously.
    # for edge in edges:
    #     DAG[edge] = 1

    # # THIS WONT WORK BECAUSE IT DOES NOT SATISFY THE DAG STRUCTURE. NEED TO USE THE SAME AS BAG 

    # return DAG
    DAG = CreateBAG(SN, N_edges)

    return DAG

def GenerateSubnetworks(SN, N, max_edges):
    '''
    params:
    SN = number of subnetworks in the network
    N = number of nodes in each subnetwork
    max_edges = maximum number of parents per node in each subnetwork 
    '''
    BAGs = []
    for i in range(SN):
        SN_DAG = GenerateBAG(N, max_edges)
        BAGs.append(SN_DAG)
    
    return BAGs

# N_SN = 4 
# BAGS, DAG = GenerateGraph(N_SN)
# start = time.time()
# CompositionalAnalysis(BAGS, DAG)
# end = time.time()
# print(f'Took {end-start} seconds for {N_SN} subnetworks')



import torch

if __name__ == '__main__':
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # nodes = []
    # times = []

    # for n in range(4, 35):
    #     nodes.append(n * 100)
    #     BAGS, DAG = GenerateGraph(n)
    #     start = time.time()
    #     ParallelCompositionalAnalysis(BAGS, DAG)
    #     end = time.time()
    #     print(f'Took {end-start} seconds for {n} subnetworks')
    #     times.append(end-start)

    # n = 3500
    # BAGS, DAG = GenerateGraph(n)
    # start = time.time()
    # ParallelCompositionalAnalysis(BAGS, DAG)
    # end = time.time()
    # print(f'Took {end-start} seconds for {n} subnetworks')
    # times.append(end-start)
    
    # plt.title('Compositional Analysis')
    # plt.plot(np.array(nodes), np.array(times), marker='x')
    # plt.xlabel('Number of nodes')
    # plt.ylabel('Inference time (s)')
    # plt.savefig('data/PARALLEL-Compositional-100-LBP-Sum-5000.png')

        
    # for n in range(4, 50):
    #     nodes.append(n * 50)
    #     BAGS, DAG = GenerateGraph(n)
    #     start = time.time()
    #     ParallelCompositionalAnalysis(BAGS, DAG)
    #     end = time.time()
    #     print(f'Took {end-start} seconds for {n} subnetworks')
    #     times.append(end-start)

    # plt.title('Compositional Analysis')
    # plt.plot(np.array(nodes), np.array(times), marker='x')
    # plt.xlabel('Number of nodes')
    # plt.ylabel('Inference time (s)')
    # plt.savefig('data/PARALLEL-Compositional-50-LBP-MAX.png')

    # Original Sequential

    # for n in range(4, 50):
    #     nodes.append(n * 50)
    #     BAGS, DAG = GenerateGraph(n)
    #     start = time.time()
    #     CompositionalAnalysis(BAGS, DAG)
    #     end = time.time()
    #     print(f'Took {end-start} seconds for {n} subnetworks')
    #     times.append(end-start)

    # Test
    # BAGS, DAG = GenerateGraph(10)
    # print(DAG)
    # ParallelCompositionalAnalysis(BAGS, DAG)

    import argparse 

    parser = argparse.ArgumentParser(description='Compositional Analysis of Bayesian Attack Graphs.')

    parser.add_argument('--output', type=str, help='Output file for the analysis.')
    parser.add_argument('--num_subnets', type=int, help='Number of subnetworks in the network.')
    parser.add_argument('--num_nodes', type=int, help='Number of nodes in each subnetwork.')
    parser.add_argument('--num_iterations', type=int, help='Number of iterations for the analysis.')
    parser.add_argument('--max_pa', type=int, help='Maximum number of parents per node.')

    # Parse arguments
    args = parser.parse_args()

    output_path = args.output
    num_subnets = args.num_subnets
    num_nodes = args.num_nodes
    num_iterations = args.num_iterations
    max_pa = args.max_pa

    # Run inference
    BAGS, DAG = GenerateGraph(num_subnets, num_nodes, max_pa)
    start = time.time()
    ParallelCompositionalAnalysis(BAGS, DAG, num_iterations)
    end = time.time()

    # Save result to file
    try:
        inference_time = end - start 
        print(f'Took {inference_time} seconds for {num_subnets} subnetworks with {num_nodes} nodes each.')
        
        with open(output_path, 'a') as f:
            f.write(f'{inference_time}\n')
        print(f'Inference time {inference_time} successfully written to {output_path}')
    except Exception as e:
        print(f'An error occurred: {e}')
