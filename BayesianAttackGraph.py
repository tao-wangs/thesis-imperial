import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt
import networkx as nx
from pgmpy.models import BayesianNetwork
from createANDtable import create_AND_table
from createORtable import create_OR_table
from drawRandomCVSS import draw_random_CVSS
from pgmpy.factors.discrete import TabularCPD

rn.seed(1)

def CreateBAG(N, max_edges):
    """
    Create the adjacency matrix (at random, limiting the number of parents per node to max_edges)
    
    # Visualisation purposes
    # i   dif  aux 
    # 2   1   [1]
    # 3   2   [1,2]
    # 4   3   [1,2,3]
    # 5   4   [1,2,3,4]

    params:
    N: Number of nodes in the Bayesian Attack Graph
    max_edges: Maximum number of parents allowed per node in the Bayesian Attack Graph
    """
    
    # Initialise adjacency matrix
    DAG = np.zeros([N, N], dtype=int)

    for i in range(1, N):
        # Randomly decide how many parents the node has 
        parents = rn.randint(1, max_edges+1)
        # Enumerate all of the parent indices 0 to node-1
        aux = np.arange(0,i) 
        # Shuffle parent indices
        rn.shuffle(aux)
        # Take first min(parents, len(aux)) indices to be parents
        ind = aux[:min(parents, len(aux))]
        # Set entries in adjacency matrix
        DAG[ind, i] = 1

    return DAG
    

def plotConnectivityMatrix(A):
    """
    Plots connectivity matrix for BAG 
    """

    y, x = np.where(A > 0)
    print(list(zip(y, x)))
    plt.scatter(x, y)
    plt.xlabel('to')
    plt.ylabel('from')
    plt.ylim(N, 0)
    plt.xlim(0, N)
    plt.tight_layout()
    plt.show()

# model.get_random_cpds()
    
def GenerateBAG(N, max_edges):
    # 1. Create DAG
    DAG = CreateBAG(N, max_edges)

    # Names of the nodes (in this case, just the number of the node but can easily be modified)
    nodes = list(range(1, N))
    # plotConnectivityMatrix(DAG)
    s, t = np.where(DAG > 0)
    edges = list(zip(s, t))

    # Visualise the network
    # G = nx.DiGraph()
    # G.add_nodes_from(nodes)
    # G.add_edges_from(edges)

    # pos = nx.spring_layout(G)
    # nx.draw(G, pos=pos, with_labels=True)
    # plt.show()

    # Initialise Bayesian Network
    model = BayesianNetwork(edges)

    # 2. Create CPDs according to specification 
    # Probability of having AND-type conditional probability tables
    pAND = 0.2 

    for i in range(N):
        npa = np.sum(DAG[:, i])
        r = rn.rand() > pAND
        
        print(f'i = {i} has {npa} parents')
        #We draw the probability from the distribution of CVSS scores
        probs = draw_random_CVSS(npa)
        if r:
            print('Creating OR table')
            cpt = create_OR_table(probs)
        else:
            print('Creating AND table')
            cpt = create_AND_table(probs)
        
        if npa:
            cpd = TabularCPD(i, 2, cpt.T, evidence=np.where(DAG[:,i])[0], evidence_card=2*np.ones(npa))
        else:
            cpd = TabularCPD(i, 2, cpt.T)
        #Insert the conditional probability table into the Bayesnet object
        model.add_cpds(cpd)
        print(cpd)
    
    return model


def ToMarkov(model):
    # 3. Create Markov Network through pgmpy's moralization
    mrf = model.to_markov_model()

    # 4. Create Factor Graph through pgmpy's functions

    factors = mrf.get_factors()
    # print(len(factors))
    for f in factors:
        print(f)
        print(f.variables)
        print(f.values)
        # print(np.log(f.values))
        print(f.values.flatten())

    return mrf

# 5. Check the factors and try to derive relationship between them

# -----------------------------------------------------------------------------
# 6. Begin inference 

import functools
import itertools

import jax
import matplotlib.pyplot as plt
import numpy as np

# Load PGMax
from pgmax import fgraph, fgroup, infer, vgroup, factor
from time import time 

# My implementation
    
def CreateFactorGraph(mrf):
    variables = vgroup.VarDict(num_states=2, variable_names=tuple(mrf.nodes))
    fg = fgraph.FactorGraph(variable_groups=[variables])

    for f in mrf.get_factors():
        npa = len(f.variables)
        fact = factor.EnumFactor(
        variables=[variables[i] for i in list(f.variables)],
        factor_configs=np.array(list(itertools.product(np.arange(2), repeat=npa))),
        log_potentials=np.log(f.values.flatten()),
        )
        
        fg.add_factors(fact)

    return fg

def RunLBP(fg, MAP=False):
    bp = infer.build_inferer(fg.bp_state, backend="bp")
    start_time=time()
    bp_arrays = bp.run(bp.init(), num_iters=100, damping=0.5, temperature=1.0)
    beliefs = bp.get_beliefs(bp_arrays)
    marginals = infer.get_marginals(beliefs)
    end_time=time()
    print(marginals)

    print(f'Time for Sum-Product LBP: {end_time-start_time} seconds')

    # bp = infer.build_inferer(fg.bp_state, backend="bp")
    # start_time=time()
    # bp_arrays = bp.run(bp.init(), num_iters=100, damping=0.5, temperature=0.0)
    # beliefs = bp.get_beliefs(bp_arrays)
    # map_states = infer.decode_map_states(beliefs)
    # end_time=time()
    # print(map_states)

    # print(f'Time for Max-Product LBP: {end_time-start_time} seconds')



if __name__ == '__main__':
    # Example usage:
    N = 5
    max_edges = 3

    BAG = GenerateBAG(N, max_edges)
    MRF = ToMarkov(BAG)
    FG = CreateFactorGraph(MRF)
    
    RunLBP(FG)