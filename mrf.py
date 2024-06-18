import numpy as np

class PairwiseMRF:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = np.zeros((num_nodes, num_nodes))
        self.node_potentials = np.zeros(num_nodes)
        self.edge_potentials = np.zeros((num_nodes, num_nodes))

    def set_node_potentials(self, potentials):
        self.node_potentials = potentials

    def set_edge_potentials(self, potentials):
        self.edge_potentials = potentials

    def add_edge(self, node1, node2):
        self.adj_matrix[node1, node2] = 1
        self.adj_matrix[node2, node1] = 1

    def compute_energy(self, assignment):
        energy = 0
        for i in range(self.num_nodes):
            energy += self.node_potentials[i, assignment[i]]
            for j in range(i+1, self.num_nodes):
                energy += self.edge_potentials[i, j, assignment[i], assignment[j]]
        return energy

    def infer(self):
        # Implement your inference algorithm here
        pass

    def learn(self, data):
        # Implement your learning algorithm here
        pass

# Example usage:
mrf = PairwiseMRF(num_nodes=3)
mrf.set_node_potentials(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
mrf.set_edge_potentials(np.array([[[0, 1, 2], [3, 4, 5], [6, 7, 8]],
                                  [[9, 10, 11], [12, 13, 14], [15, 16, 17]],
                                  [[18, 19, 20], [21, 22, 23], [24, 25, 26]]]))
mrf.add_edge(0, 1)
mrf.add_edge(1, 2)

assignment = [0, 1, 2]
energy = mrf.compute_energy(assignment)
print("Energy:", energy)