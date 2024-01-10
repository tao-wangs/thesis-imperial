from BayesianAttackGraph import * 
import numpy as np
import matplotlib.pyplot as plt 

N = 200
max_edges = 3

nodes = np.arange(1, N)
times = np.zeros(len(nodes))

for n in range(2, N):
    print(f'Running LBP for {n} nodes')
    BAG = GenerateBAG(n, max_edges)
    MRF = ToMarkov(BAG)
    FG = CreateFactorGraph(MRF)
    t = RunLBP(FG)
    times[n-1] = t

plt.title('Loopy Belief Propagation')
plt.plot(nodes, times)
plt.xlabel('Number of nodes')
plt.ylabel('Inference time (s)')
plt.show()