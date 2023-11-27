import numpy as np
import matplotlib.pyplot as plt

# Number of nodes in the Bayesian Attack Graph
N = 20
# Maximum number of parents allowed per node in the Bayesian Attack Graph
max_edges = 3

# Initialise adjacency matrix
DAG = np.zeros([N, N], dtype=int)


def createDAG():
    """
    Create the adjacency matrix (at random, limiting the number of parents per node to max_edges)
    
    # Visualisation purposes
    # i   dif  aux 
    # 2   1   [1]
    # 3   2   [1,2]
    # 4   3   [1,2,3]
    # 5   4   [1,2,3,4]
    """

    for i in range(1, N):
        # Randomly decide how many parents the node has 
        parents = np.random.randint(1, max_edges+1)
        # Enumerate all of the parent indices 0 to node-1
        aux = np.arange(0,i) 
        # Shuffle parent indices
        np.random.shuffle(aux)
        # Take first min(parents, len(aux)) indices to be parents
        ind = aux[:min(parents, len(aux))]
        # Set entries in adjacency matrix
        DAG[ind, i] = 1
    

def plotConnectivityMatrix(A):
    """
    Plots connectivity matrix for excitatory modules. 
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


createDAG()
plotConnectivityMatrix(DAG)



