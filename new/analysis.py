import itertools
import jax
import jax.numpy as jnp
import matplotlib.pyplot as plt
import numpy as np 
from pgmax import fgraph, vgroup, factor, infer
import time

def create_factor_graph(num_nodes):
    nodes = list(range(num_nodes))
    variables = vgroup.VarDict(num_states=2, variable_names=nodes)
    fg = fgraph.FactorGraph(variable_groups=[variables])
    
    # Generate all possible binary and ternary factor configurations
    unary_factor_configs = np.array(list(itertools.product(np.arange(2), repeat=1)))
    binary_factor_configs = np.array(list(itertools.product(np.arange(2), repeat=2)))
    ternary_factor_configs = np.array(list(itertools.product(np.arange(2), repeat=3)))

    # Add a single ternary factor connecting all nodes
    if num_nodes >= 3:
        DEF = factor.EnumFactor(
            variables=[variables[i] for i in range(3)],
            factor_configs=ternary_factor_configs, 
            log_potentials=np.log(np.array([1, 0, 0, 0.03808, 0, 0.454, 0.05848, 0.23392]))
        )
        fg.add_factors([DEF])
    
    return fg, variables

def run_inference(fg, variables):
    bp = infer.BP(fg.bp_state, temperature=1.0)
    bp_arrays = bp.init()
    start_time = time.time()
    bp_arrays = bp.run(bp_arrays, num_iters=50, damping=0.5)
    end_time = time.time()
    return end_time - start_time

def scalability_analysis(max_nodes=1000, step=2):
    node_counts = list(range(3, max_nodes+1, step))
    inference_times = []

    for num_nodes in node_counts:
        fg, variables = create_factor_graph(num_nodes)
        inference_time = run_inference(fg, variables)
        inference_times.append(inference_time)
        print(f"Number of nodes: {num_nodes}, Inference time: {inference_time:.4f} seconds")

    plt.plot(node_counts, inference_times, marker='o')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Inference Time (seconds)')
    plt.title('Scalability Analysis of Belief Propagation Inference')
    plt.grid(True)
    plt.show()

scalability_analysis(max_nodes=1000, step=2)


