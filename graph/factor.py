
class FactorGraph:
    def __init__(self):
        self.var_nodes = []
        self.factor_nodes = []

    def update_beliefs(self):
        for node in self.var_nodes:
            node.update_belief()

    def update_ellipses(self):
        for node in self.var_nodes:
            node.update_ellipse()

    def send_messages(self):
        for node in self.factor_nodes:
            node.send_message()

    def sync_iter(self):
        self.send_messages()
        self.update_beliefs()
        self.update_ellipses()
    
    def find_node(self, name):
        for node in self.var_nodes:
            if node.name == name:
                return node
        return None

    def find_edge(self, name):
        for node in self.factor_nodes:
            if node.name == name:
                return node
        return None
    
    def find_factor(self, name):
        for node in self.factor_nodes:
            if node.name == name:
                return node
        return None
    
    def remove_node(self, node):
        if node in self.var_nodes:
            self.var_nodes.remove(node)
        elif node in self.factor_nodes:
            self.factor_nodes.remove(node)
        else:
            print("Node not found in graph")
    
    def update_node_ids(self):
        for i, node in enumerate(self.var_nodes):
            node.id = i
        for i, node in enumerate(self.factor_nodes):
            node.id = i
    
    def compute_error(self):
        error = 0
        for node in self.var_nodes:
            error += node.compute_error()
        return error

    def priors_to_gt(self):
        for node in self.var_nodes:
            node.prior_to_gt()
        
    def compute_MAP(self):
        for node in self.var_nodes:
            node.compute_MAP()
    
    def compare_to_MAP(self):
        for node in self.var_nodes:
            node.compare_to_MAP()
    
    def update_priors(self):
        for node in self.var_nodes:
            node.update_prior()
    
    def update_factor_noise_models(self):
        for node in self.factor_nodes:
            node.update_noise_model()

    def add_var_node(self, node):
        self.var_nodes.append(node)
    
    def add_factor_node(self, node):

    def add_linear_factor(self, name, var1, var2, mean, covar):
        factor = LinearFactor(name, var1, var2, mean, covar)
        self.factor_nodes.append(factor)
        return factor