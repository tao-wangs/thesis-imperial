
import argparse
import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt


def create_stochastic_block_model(n, b_size, p_matrix):
    """
    Generates a stochastic block model graph
    
    Parameters:
    n (int): Number of nodes in the graph.
    b_size ([int]): List containing the sizes of each block.
    p_matrix (np.array): Matrix containing the probabilities of edges between blocks.

    Returns:
    G: Generated stochastic block model graph.
    """
    # Sanity check
    assert sum(b_size) == n, "Sum of block sizes must be equal to the number of nodes."

    # SBM creation 
    G = nx.stochastic_block_model(b_size, p_matrix)

    return G 


def __main__():
    parser = argparse.ArgumentParser(description='Evaluating the scalability of MRF model.')

    # Arguments
    parser.add_argument('--max_nodes', type=int, default=1000, help='Maximum number of nodes in the MRF model.')

    # Parse arguments
    args = parser.parse_args()

    # Use the arguments
    max_nodes = args.max_nodes

    scalability_analysis(max_nodes=max_nodes)


# Parameters
n = 100  # Total number of nodes
sizes = [40, 30, 30]  # Sizes of the blocks
p_matrix = np.array([[0.8, 0.05, 0.02], [0.05, 0.7, 0.03], [0.02, 0.03, 0.6]])  # Probability matrix

# Generate SBM
G = create_stochastic_block_model(n, sizes, p_matrix)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=50, node_color="skyblue", edge_color="gray")
plt.show()