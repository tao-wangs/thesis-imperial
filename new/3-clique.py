# Simple baseline example involving two variables 

# this is the implementation for the original file 

import itertools
import jax
import matplotlib.pyplot as plt
import numpy as np 
from pgmax import fgraph, vgroup, factor, infer

# N = 10
# nodes = ['D', 'E', 'F']
nodes = list(range(3))
variables = vgroup.VarDict(num_states=2, variable_names=nodes)
fg = fgraph.FactorGraph(variable_groups=[variables])   

# Add pairwise factors e.g:
# array([[0, 0],
#        [0, 1],
#        [1, 0],
#        [1, 1]])
unary_factor_configs = np.array(list(itertools.product(np.arange(2), repeat=1)))
binary_factor_configs = np.array(list(itertools.product(np.arange(2), repeat=2)))
ternary_factor_configs = np.array(list(itertools.product(np.arange(2), repeat=3)))

# add factors 

# A1B
DEF = factor.EnumFactor(
        variables = [variables[0], variables[1], variables[2]],
        factor_configs = ternary_factor_configs, 
        # log_potentials = np.log(np.array([3, 0.8, 0.34, 1.28, 0.86, 2.32, 1.4, 2]))
        # log_potentials = np.log(np.array([1, 0, 0, 0.03808, 0, 0.454, 0.05848, 0.23392]))
        # New example with 0.6 for all 3. 
        # log_potentials = np.log(np.array([3, 0.8, 0.8, 1.360, 0.8, 1.360, 1.360, 2.520]))
        # log_potentials = np.log(np.array([2.565, 0.829, 0.829, 1.453, 0.829, 1.453, 1.453, 2.589]))
        # log_potentials = np.log(np.array([3, 2, 2, 0.64, 2, 0.75, 0.84, 0.77]))
        log_potentials = np.log(np.array([2.565, 1.855, 1.855, 0.834, 1.855, 0.927, 1.004, 1.105]))
     )

fg.add_factors([DEF])


bp = infer.BP(fg.bp_state, temperature=1.0)
# bp_arrays = bp.init()
bp_arrays = bp.init(evidence_updates={variables[0]: np.array([0., 100])})
bp_arrays = bp.run(bp_arrays, num_iters=50, damping=0.5)
beliefs = bp.get_beliefs(bp_arrays)
marginals = infer.get_marginals(beliefs)

for key, array in list(marginals.values())[0].items():
    print(f"Key {key}: {array}")



# pz = 0.05
# pe = 0.10
# p_l = 1 - (1-pz)*(1-pe)

# pv = 0.6 
# FFF, FFT, FTF, FTT, TFF, TFT, TTF, TTT
# P (A | B, C)
