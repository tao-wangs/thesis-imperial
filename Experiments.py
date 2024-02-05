from BayesianAttackGraph import * 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 
import time 

from pgmpy.inference import BeliefPropagation

N = 6
max_edges = 3

nodes = []
times = []

times_jt = np.zeros(len(nodes))

for n in range(2, N, 50):
    nodes.append(n)
    print(f'Running LBP for {n} nodes')
    BAG = GenerateBAG(n, max_edges)
    MRF = ToMarkov(BAG)
    FG = CreateFactorGraph(MRF)
    t = RunLBP(FG)
    times.append(t)

    print(BAG)

# plt.title('Loopy Belief Propagation')
# plt.plot(np.array(nodes), np.array(times), marker='x')
# plt.xlabel('Number of nodes')
# plt.ylabel('Inference time (s)')
# plt.savefig('data/P-LBP-Sum.png')

# nodes = []
# times = []

# for n in range(2, N, 50):
#     nodes.append(n)
#     print(f'Running LBP for {n} nodes')
#     BAG = GenerateBAG(n, max_edges)
#     MRF = ToMarkov(BAG)
#     FG = CreateFactorGraph(MRF)
#     t = RunLBP(FG, MAP=True)
#     times.append(t)

# plt.clf()
# plt.title('Loopy Belief Propagation')
# plt.plot(np.array(nodes), np.array(times), marker='x')
# plt.xlabel('Number of nodes')
# plt.ylabel('Inference time (s)')
# plt.savefig('data/P-LBP-Max.png')

# print(f'Running JT for {N} nodes')

# BAG = GenerateBAG(N, max_edges)
# MRF = ToMarkov(BAG)
# FG = CreateFactorGraph(MRF)

# start = time.time()
# BP = BeliefPropagation(BAG)
# print(BAG.nodes)
# BP.query(BAG.nodes)
# end = time.time()
# elapsed = end - start 
# print(f'Took {elapsed} seconds')
# times_jt[n-1] = elapsed