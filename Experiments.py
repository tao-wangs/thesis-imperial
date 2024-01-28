from BayesianAttackGraph import * 
import numpy as np
import matplotlib.pyplot as plt 
import time 

from pgmpy.inference import BeliefPropagation

N = 500
max_edges = 3

nodes = np.arange(1, N)
times = np.zeros(len(nodes))

times_jt = np.zeros(len(nodes))

for n in range(2, N, 50):
    print(f'Running LBP for {n} nodes')
    BAG = GenerateBAG(n, max_edges)
    MRF = ToMarkov(BAG)
    FG = CreateFactorGraph(MRF)
    t = RunLBP(FG, MAP=True)
    times[n-1] = t

    print(f'Running JT for {n} nodes')

    start = time.time()
    BP = BeliefPropagation(BAG)
    print(BAG.nodes)
    BP.query(variables=BAG.nodes, evidence=None)
    end = time.time()
    elapsed = end - start 
    times_jt[n-1] = elapsed


plt.title('Loopy Belief Propagation')
plt.plot(nodes, times)
plt.xlabel('Number of nodes')
plt.ylabel('Inference time (s)')
plt.show()