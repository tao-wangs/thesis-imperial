# Simple baseline example involving two variables 

# this is the implementation for the original file 

import itertools
import jax
import matplotlib.pyplot as plt
import numpy as np 
from pgmax import fgraph, vgroup, factor, infer

# N = 10
# nodes = ['A', 'B']
nodes = list(range(2))
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

AB = factor.EnumFactor(
        variables = [variables[0], variables[1]],
        factor_configs = binary_factor_configs, 
        # log_potentials = np.log(np.array([1.8, 0.24, 0.24, 1.72]))
        # log_potentials = np.log(np.array([1.8, 0.226, 0.226, 1.748]))
        # log_potentials = np.log(np.array([1.8, 0.82, 0.64, 0.74]))
        # log_potentials=np.log(np.array([1.8, 0.64, 1.0, 0.56]))
        # log_potentials=np.log(np.array([2, 0.6, 1.0, 0.4]))
        # log_potentials = np.log(np.array([0.2, 0.4, 0, 0]))
        # log_potentials=np.log(np.array([2.0, 0.6, 0.5, 0.9]))
     )

fg.add_factors([AB])


bp = infer.BP(fg.bp_state, temperature=1.0)
bp_arrays = bp.init()
# bp_arrays = bp.init(evidence_updates={variables[1]: np.array([0., 100])})
bp_arrays = bp.run(bp_arrays, num_iters=50, damping=0.5)
beliefs = bp.get_beliefs(bp_arrays)
marginals = infer.get_marginals(beliefs)

for key, array in list(marginals.values())[0].items():
    print(f"Key {key}: {array}")