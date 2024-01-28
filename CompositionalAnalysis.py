import numpy as np
from BayesianAttackGraph import GenerateBAG

def CompositionalAnalysis(SN):
    number_of_subnets = len(SN)
    #initialise 
    analysis_enabled = False * np.array(number_of_subnets)
    analysis_computed = False * np.array(number_of_subnets)
    parent_subneworks_computed = False * np.array(number_of_subnets)

    for i in range(number_of_subnets):
        analysis_enabled[i] = check_parent_subnetworks(SN[i], parent_subneworks_computed[i])
    
    while analysis_computed:
        for i in range(number_of_subnets):
            analysis_enabled[i] = check_parent_subnetworks(SN[i], parent_subneworks_computed[i])
            if analysis_enabled[i] and not analysis_computed[i]:
                compute_probabilities(SN[i])
                analysis_computed[i] = True
                update_children_subnetworks(parent_subneworks_computed, SN)
    
    # return updated BAG model with the estimated unconditional probabilities 
    return SN 


def GenerateGraph(SN):
    '''
    params:

    SN = number of subnets 
    '''
    # High level representation 


    
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

    # Initialise weight and matrix for the network 
    W = np.zeros((SN, SN))

    # Generate all possible edges to sample from 
    all_edges = []
    for i in range(SN):
        for j in range(SN):
            if i == j:
                continue
            all_edges.append((i, j))

    # Uniformly sample N_edges connections 
    idxs = np.random.choice(len(all_edges), size=N_edges, replace=False)
    edges = [all_edges[idx] for idx in idxs]
    
    # Maximum number of parent nodes for each node. 

    # Set connection weight to be 1 for randomly generated connections
    # Set random delays for these connections simultaneously.
    for edge in edges:
        W[edge] = 1

    return W 

def GenerateSubnetworks(SN, N, max_edges):
    '''
    params:
    SN = number of subnetworks in the network
    N = number of nodes in each subnetwork
    max_edges = maximum number of parents per node in each subnetwork 
    '''
    BAGs = []
    for subnet in SN:
        SN_DAG = GenerateBAG(N, max_edges)
        BAGs.append(SN_DAG)