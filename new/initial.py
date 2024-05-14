import itertools
import jax
import matplotlib.pyplot as plt
import numpy as np 
from pgmax import fgraph, vgroup, factor, infer

# N = 10
# nodes = ['A1', 'A2', 'B', 'C', 'D', 'E', 'F']
nodes = list(range(7))
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
A1B = factor.EnumFactor(
        variables = [variables[0], variables[2]],
        factor_configs = binary_factor_configs, 
        log_potentials = np.log(np.array([0., 0., 0.5, 1.]))
     )

A2C = factor.EnumFactor(
        variables = [variables[1], variables[3]],
        factor_configs = binary_factor_configs, 
        log_potentials = np.log(np.array([0., 0., 0.7, 1.]))
    )

BD = factor.EnumFactor(
        variables = [variables[2], variables[4]],
        factor_configs = binary_factor_configs, 
        log_potentials = np.log(np.array([0.5, 0.1, 0.1, 1.]))
    )

CD = factor.EnumFactor(
        variables = [variables[3], variables[4]],
        factor_configs = binary_factor_configs, 
        log_potentials = np.log(np.array([0.5, 0.1, 0.1, 1.]))
    )

CE = factor.EnumFactor(
        variables = [variables[3], variables[5]],
        factor_configs = binary_factor_configs, 
        log_potentials = np.log(np.array([0.5, 0.1, 0.1, 1.]))
    )

DEF = factor.EnumFactor(
        variables = [variables[4], variables[5], variables[6]],
        factor_configs = ternary_factor_configs, 
        log_potentials = np.log(np.array([1., 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 1.]))
    )

fg.add_factors([A1B, A2C, BD, CD, CE, DEF])

# fg.add_factor(
#     variables = ['D', 'E'],
#     factor_configs = binary_factor_configs, 
#     log_potentials = np.log(np.array([0, 0, 0, 0])), 
# )

# # EF
# fg.add_factor(
#     variables = ['E', 'F'],
#     factor_configs = binary_factor_configs, 
#     log_potentials = np.log(np.array([0, 0, 0, 0])), 
# )

flag = False 
# run MAP inference algorithm
# bp = infer.build_inferer(fg.bp_state, backend="bp")
# bp_arrays = bp.run(bp.init(), num_iters=100, damping=0.5, temperature=0.0)
# beliefs = bp.get_beliefs(bp_arrays)
# map_states = infer.decode_map_states(beliefs)   

# run Sum-Product inference algorithm
# bp = infer.build_inferer(fg.bp_state, backend="bp")
# bp_arrays = bp.run(bp.init(), num_iters=50, damping=0.5, temperature=1.0)
# beliefs = bp.get_beliefs(bp_arrays)
# marginals = infer.get_marginals(beliefs)

# for key, array in list(marginals.values())[0].items():
#     print(f"Key {key}: {array}")

# incorporate evidence

# fg.bp_state.evidence[variables[4]] = np.array([0, 1.])
# bp = infer.build_inferer(fg.bp_state, backend="bp")
# bp_arrays = bp.run(bp.init(), num_iters=50, damping=0.5, temperature=1.0)
# beliefs = bp.get_beliefs(bp_arrays)
# marginals = infer.get_marginals(beliefs)

# for key, array in list(marginals.values())[0].items():
#     print(f"Key {key}: {array}")

bp = infer.BP(fg.bp_state, temperature=1.0)
# bp_arrays = bp.init()
bp_arrays = bp.init(evidence_updates={variables[4]: np.array([0, 100.])})
bp_arrays = bp.run(bp_arrays, num_iters=100, damping=0.5)
beliefs = bp.get_beliefs(bp_arrays)
marginals = infer.get_marginals(beliefs)

for key, array in list(marginals.values())[0].items():
    print(f"Key {key}: {array}")