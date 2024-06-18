import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create or load a graph
# Creating a sample graph
G = nx.erdos_renyi_graph(n=10, p=0.5, seed=42)  # You can also load a graph from a file

# Step 2: Find all cliques
cliques = list(nx.find_cliques(G))

# Print all cliques
print("All cliques in the graph:")
for clique in cliques:
    print(clique)

# Step 3: Visualize the graph and highlight the cliques
# Define a color map to differentiate cliques
color_map = []
for node in G:
    found_in_clique = False
    for clique in cliques:
        if node in clique:
            found_in_clique = True
            color_map.append('lightgreen')  # Highlight clique nodes
            break
    if not found_in_clique:
        color_map.append('lightblue')  # Non-clique nodes

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color=color_map, with_labels=True, node_size=500, font_size=10, font_color='black', edge_color='gray')
plt.title("Graph with Cliques Highlighted")
plt.show()
