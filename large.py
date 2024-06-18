from pgmpy.models import BayesianNetwork, MarkovNetwork
from pgmpy.inference import VariableElimination, BeliefPropagation
import time
import random 

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

num_nodes = 100 
num_edges = 1000
edges = []

i = 0
# Generate 1000 edges randomly between nodes
while i < num_edges:
    node1 = random.randint(0, num_nodes - 1)
    node2 = random.randint(0, num_nodes - 1)
    if node1 != node2 and not (node1, node2) in edges:
        edges.append((node1, node2))
        i+= 1

values = pd.DataFrame(np.random.randint(low=0, high=2, size=(1000, num_nodes)),
                      columns=[str(item) for item in range(num_nodes)])

edges = [(str(item[0]), str(item[1])) for item in edges]
model = MarkovNetwork(edges)
model.fit(values)
ve = VariableElimination(model)

start_time = time.time()
phi_query = ve.query(['A', 'B'])
end_time = time.time()
print(f'Time for Variable Elimination Algorithm: {end_time - start_time} s')
print(phi_query)

jt = BeliefPropagation(model)
start_time = time.time()
phi_query = jt.query(['A', 'B'])
end_time = time.time()
print(f'Time for Junction Tree Algorithm: {end_time - start_time} s')
print(phi_query)