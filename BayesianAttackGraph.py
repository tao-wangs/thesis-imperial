import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt
import networkx as nx
from pgmpy.models import BayesianNetwork, MarkovNetwork
from utils import createANDtable, createORtable, drawRandomCVSS
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
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True)
plt.show()

# Initialise Bayesian Network
model = BayesianNetwork(edges)

# 2. Create CPDs according to specification 
# Probability of having AND-type conditional probability tables
pAND = 0.2 

for i in range(N):
    npa = np.sum(DAG[:, i])
    r = rn.rand() > pAND
    
    #We draw the probability from the distribution of CVSS scores
    probs = drawRandomCVSS(npa)
    if r:
        cpt = createORtable(probs)
    else:
        cpt = createANDtable(probs)
    
    cpd = TabularCPD(f'{i}', 2, cpt.T, evidence=np.where(DAG[:,i]), evidence_card=2*np.ones(npa))
    #Insert the conditional probability table into the Bayesnet object
    model.add_cpds(cpd)
    print(cpd)

# 3. Create Markov Network through pgmpy's moralization
# 4. Create Factor Graph through pgmpy's functions
# 5. Check the factors and try to derive relationship between them
