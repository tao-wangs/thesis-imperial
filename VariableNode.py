import torch

class Gaussian:
    def __init__(self, eta, lmbda):
        self.eta = eta
        self.lmbda = lmbda

    def getCovariance(self):
        return torch.inverse(self.lmbda)
    
    def getMean(self):
        cov = self.getCovariance()
        return cov.matmul(self.eta)
    
    def product(self, gaussian):
        self.eta.add(gaussian.eta)
        self.lmbda.add(gaussian.lmbda)



class VariableNode:
    def __init__(self, id, dofs):
        self.id = id
        self.note = ''
        self.type = 'var_node'
        self.belief = Gaussian(torch.zeros(dofs, 1), torch.zeros(dofs, dofs))
        self.prior = Gaussian(torch.zeros(dofs, 1), torch.zeros(dofs, dofs))
        self.adj_ids = []

    def computeBelief(self, G):
        self.belief.eta = self.prior.eta.clone()
        self.belief.lmbda = self.prior.lmbda.clone()
        for i in range(len(self.adj_ids)):
            factor_node = G.find_node(self.adj_ids[i])
            idx = factor_node.adj_ids.indexOf(self.id)
            factor_node.adj_beliefs[idx] = self.belief

    def sendBelief(self, G):
        for i in range()

