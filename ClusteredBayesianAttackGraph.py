import numpy as np
import numpy.random as rn

# Number of clusters for the Bayesian Attack Graph
Nclusters = 4
# Number of nodes per cluster
N = 10 
# Total number of nodes in the Bayesian Attack Graph
Ntot = Nclusters * N 

# Initialise the adjacency matix
DAG = np.zeros([Ntot, Ntot])

# Maximum number of parents allowed per node in the BAG
max_edges = 3 

# Create the adjacency matrix
for j in range(Nclusters):
    DAG2 = np.zeros([N, N])
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
        DAG2[ind, i] = 1
    DAG[N*(j-1)+1:N*(j-1)+N, N*(j-1)+1:N*(j-1)+N] = DAG2
    c1 = np.arange(0,Ntot)
    c2 = np.arange(N*(j-1)+1,N*(j-1)+N)
    c1 = setdiff(c1, c2)
    perm = randperm(len(c1))
    c1 = c1(perm)
    rd = randi([N*(j-1)+1, N*(j-1)+N])
    if rd > c1(0):
        DAG[c1[0], rd] = 1 
    else:
        DAG[rd, c1[0]] = 1
    
    