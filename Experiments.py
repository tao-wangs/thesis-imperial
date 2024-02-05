from BayesianAttackGraph import * 
import numpy as np
import matplotlib.pyplot as plt 
import time 

from pgmpy.inference import BeliefPropagation

N = 200
max_edges = 3

nodes = np.arange(1, N)
times = np.zeros(len(nodes))

times_jt = np.zeros(len(nodes))

for n in range(2, N):
    print(f'Running LBP for {n} nodes')
    BAG = GenerateBAG(n, max_edges)
    MRF = ToMarkov(BAG)
    FG = CreateFactorGraph(MRF)
    t, _ = RunLBP(FG)
    times[n-1] = t

    print(f'Running JT for {n} nodes')

    start = time.time()
    BP = BeliefPropagation(BAG)
    print(BAG.nodes)
    BP.query(variables=BAG.nodes, evidence=None)
    end = time.time()
    elapsed = end - start 
    times_jt[n-1] = elapsed

    JT = BeliefPropagation(BAG)
    start_time = time.time()
    phi_query = JT.map_query(list(BAG.nodes))
    end_time = time.time()
    print(f'Time for Junction Tree Algorithm: {end_time - start_time} s')
    print(phi_query)



# plt.title('Loopy Belief Propagation')
# plt.plot(nodes, times)
# plt.xlabel('Number of nodes')
# plt.ylabel('Inference time (s)')
# plt.show()