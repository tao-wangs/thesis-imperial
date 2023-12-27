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

N = 10 
max_edges = 3

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

# model.get_random_cpds()
    
# 3. Create Markov Network through pgmpy's moralization
mrf = model.to_markov_model()

# 4. Create Factor Graph through pgmpy's functions

fg = mrf.to_factor_graph()

# 5. Check the factors and try to derive relationship between them

# -----------------------------------------------------------------------------
# 6. Begin inference 

import functools

import jax
# import matplotlib.pyplot as plt
# import numpy as np

############
# Load PGMax
from pgmax import fgraph, fgroup, infer, vgroup

# Load data
folder_name = "example_data/"
params = np.load(open(folder_name + "rbm_mnist.npz", 'rb'), allow_pickle=True)
bv = params["bv"]
bh = params["bh"]
W = params["W"]

# Initialize factor graph
hidden_variables = vgroup.NDVarArray(num_states=2, shape=bh.shape)
visible_variables = vgroup.NDVarArray(num_states=2, shape=bv.shape)
fg = fgraph.FactorGraph(variable_groups=[hidden_variables, visible_variables])

# Create unary factors
hidden_unaries = fgroup.EnumFactorGroup(
    variables_for_factors=[[hidden_variables[ii]] for ii in range(bh.shape[0])],
    factor_configs=np.arange(2)[:, None],
    log_potentials=np.stack([np.zeros_like(bh), bh], axis=1),
)
visible_unaries = fgroup.EnumFactorGroup(
    variables_for_factors=[[visible_variables[jj]] for jj in range(bv.shape[0])],
    factor_configs=np.arange(2)[:, None],
    log_potentials=np.stack([np.zeros_like(bv), bv], axis=1),
)

# Create pairwise factors
log_potential_matrix = np.zeros(W.shape + (2, 2)).reshape((-1, 2, 2))
log_potential_matrix[:, 1, 1] = W.ravel()

variables_for_factors = [
    [hidden_variables[ii], visible_variables[jj]]
    for ii in range(bh.shape[0])
    for jj in range(bv.shape[0])
]
pairwise_factors = fgroup.PairwiseFactorGroup(
    variables_for_factors=variables_for_factors,
    log_potential_matrix=log_potential_matrix,
)

# Add factors to the FactorGraph
fg.add_factors([hidden_unaries, visible_unaries, pairwise_factors])

bp = infer.build_inferer(fg.bp_state, backend="bp")
bp_arrays = bp.run(bp.init(), num_iters=100, damping=0.5, temperature=1.0)
beliefs = bp.get_beliefs(bp_arrays)
marginals = infer.get_marginals(beliefs)