from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination, BeliefPropagation
import time
import random 
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

N_NODES = 30 
N_EDGES = 24

SUBNET_SIZE = 10
N_SUBNETS = int(N_NODES / SUBNET_SIZE)
N_SUBNET_EDGES = int(N_EDGES / N_SUBNETS)

np.random.seed(2)

def createCommunity(N, N_edges): 

        # Initialise weight and delay matrix for excitatory commmunity
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


def connectSubnetworks(W):
    # We want n-1 communities to connect to a single subnetwork 
    for i in range(0, N_SUBNETS-1):
        
        src = np.random.randint(0, SUBNET_SIZE)
        tgt = np.random.randint(0, SUBNET_SIZE)
        
        # Find an existing edge in that subnetwork and rewire it to the final one
        while not W[i*SUBNET_SIZE+src, i*SUBNET_SIZE+tgt]:
            src = np.random.randint(0, SUBNET_SIZE)
            tgt = np.random.randint(0, SUBNET_SIZE)

        print(f'Deleting edge {i*SUBNET_SIZE+src, i*SUBNET_SIZE+tgt}')
        W[i*SUBNET_SIZE+src, i*SUBNET_SIZE+tgt] = 0
        
        while not np.isin(1, W[(N_SUBNETS-1)*SUBNET_SIZE+tgt,:]): 
            tgt = np.random.randint(0, SUBNET_SIZE)

        print(f'Adding edge {i*SUBNET_SIZE+src, (N_SUBNETS-1)*SUBNET_SIZE+tgt}')
        W[i*SUBNET_SIZE+src, (N_SUBNETS-1)*SUBNET_SIZE+tgt] = 1


def plotConnectivityMatrix(W):
        """
        Plots connectivity matrix for excitatory modules. 
        """

        y, x = np.where(W > 0)
        plt.scatter(x, y)
        plt.xlabel('to')
        plt.ylabel('from')
        plt.ylim(N_NODES, 0)
        plt.xlim(0, N_NODES)
        plt.tight_layout()
        plt.show()



W = np.zeros([N_NODES, N_NODES])

# Generate N_SUBSETS disconnected communities 
for i in range(0, N_NODES, SUBNET_SIZE):
    Wblock = createCommunity(SUBNET_SIZE, N_SUBNET_EDGES)
    W[i:i+SUBNET_SIZE, i:i+SUBNET_SIZE] = Wblock

# How do I avoid cycles? 
plotConnectivityMatrix(W)
connectSubnetworks(W)

W[4,5] = 1
W[19,15] = 1

y, x = np.where(W > 0)
edges = [(str(item[0]), str(item[1])) for item in list(zip(y, x))]
BAG = BayesianNetwork(edges)
nx.draw_circular(nx.DiGraph(edges), with_labels=True)
plt.show()

# Inference time scalability comparison. 
values = pd.DataFrame(np.random.randint(low=0, high=2, size=(1000, N_NODES)),
                      columns=[str(item) for item in np.arange(0, N_NODES)])

model = BayesianNetwork(edges)
model.fit(values)

start_time = time.time()
ve = VariableElimination(model)
phi_query = ve.query(['28', '29'])
end_time = time.time()
print(f'Time for Variable Elimination Algorithm: {end_time - start_time} s')
print(phi_query)

jt = BeliefPropagation(model)
start_time = time.time()
phi_query = jt.query(['28', '29'])
end_time = time.time()
print(f'Time for Junction Tree Algorithm: {end_time - start_time} s')
print(phi_query)
