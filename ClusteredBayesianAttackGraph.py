import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import jax
import itertools 
import time 
import argparse 

from BayesianAttackGraph import RunLBP 
from pgmax import fgraph, vgroup, factor, infer 

class SmallWorldModularNetwork(object):
    def __init__(self, p, num_nodes, num_subnets):
        """
        Initialise modular network.

        Inputs:
            p            -- Rewiring probability
            num_nodes    -- Number of nodes in a sub-network
            num_subnets  -- Number of subnets in the network
        """
        self.num_nodes = num_nodes         # Number of nodes in a sub-network 
        self.num_subnets = num_subnets     # Number of subnets in the network
        self.N = num_nodes * num_subnets   # Total number of nodes in the network

        self._p = p

        # Initialise weight adjacency matrix for modular network 
        self.W = np.zeros([self.N, self.N])

        # Update intra-subnetwork blocks
        for i in range(0, self.N, num_nodes):
            Wblock = self._intraSubnetworkConnections(num_nodes)
            self.W[i:i + num_nodes, i:i + num_nodes] = Wblock

        # Apply rewiring process
        self._rewireConnectivity()


    def _intraSubnetworkConnections(self, N):
        """
        Generates excitatory-to-excitatory connections according to specification.

        Inputs:
            N -- The number of nodes in the sub-network.

        Outputs:
            W -- The connectivity matrix for the subnetwork community.
        """

        # Number of connections in this excitatory module
        N_edges = N * 2 

        # Initialise weight and delay matrix for subnetwork 
        W = np.zeros((N, N))

        # Generate all possible edges to sample from 
        all_edges = []
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                all_edges.append((i, j))

        # Uniformly sample N_edges connections 
        idxs = np.random.choice(len(all_edges), size=N_edges, replace=False)
        edges = [all_edges[idx] for idx in idxs]

        # Set connection weight to be 1 for randomly generated connections
        # Set random delays for these connections simultaneously.
        for edge in edges:
            W[edge] = 1 

        return W


    def _rewireConnectivity(self):
        """
        Rewires the connections between subnetworks with probability p.

        Inputs:
            p  -- Rewiring probability 
        """

        src, tgt = np.where(self.W[:self.N, :self.N] > 0)
        for s, t in zip(src, tgt):
            if np.random.random() < self._p:
                self.W[s, t] = 0
                # Pick index of new node to rewire to. It can't be an existing
                # connection or itself (because the total density has to be preserved)
                h = s
                while s == h or self.W[s, h]:
                    h = np.random.randint(self.N)
                self.W[s, h] = 1 


    def plotConnectivityMatrix(self):
        """
        Plots connectivity matrix for subnetworks. 
        """

        y, x = np.where(self.W[:self.N, :self.N] > 0)
        plt.scatter(x, y, s=1)
        plt.title(f'p = {self._p}')
        plt.xlabel('to')
        plt.ylabel('from')
        plt.ylim(self.N, 0)
        plt.xlim(0, self.N)
        plt.show()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Inference on MRFs with a modular structure.')

    parser.add_argument('--output', type=str, help='Output file for the analysis.')
    parser.add_argument('--num_subnets', type=int, help='Number of subnets in the network.')
    parser.add_argument('--num_nodes', type=int, help='Number of nodes in the network.')
    parser.add_argument('--num_iterations', type=int, help='Number of iterations for the analysis.')
    parser.add_argument('--p', type=float, help='Rewiring probability.')
    parser.add_argument('--analysis_type', type=str, help='Type of analysis to run.')

    args = parser.parse_args()

    output_path = args.output
    num_subnets = args.num_subnets
    num_nodes = args.num_nodes
    num_iterations = args.num_iterations
    p = args.p
    analysis_type = args.analysis_type

    network = SmallWorldModularNetwork(p, num_nodes, num_subnets)
    ADJ = network.W 

    G = nx.from_numpy_array(ADJ)
    cliques = list(nx.find_cliques(G))

    variables = vgroup.VarDict(num_states=2, variable_names=list(nx.nodes(G)))
    FG = fgraph.FactorGraph(variable_groups=[variables])

    for clique in cliques:
        num_vars = len(clique)
        factor_configs = np.array(list(itertools.product(np.arange(2), repeat=num_vars)))
        fact = factor.EnumFactor(
            variables = [variables[i] for i in clique],
            factor_configs = factor_configs,
            log_potentials = np.log(np.random.rand(2**num_vars))
        )

        FG.add_factors(fact)

    start = time.time()
    RunLBP(FG, num_iterations=num_iterations, MAP=True, analysis_type=analysis_type)
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