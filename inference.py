# A simple Exact inference algorithm

import itertools
import time 

from pgmpy.inference.base import Inference
from pgmpy.factors import factor_product


class SimpleInference(Inference):
    # By inheriting Inference we can use self.model, self.factors and self.cardinality in our class
    def query(self, var, evidence):
        # self.factors is a dict of the form of {node: [factors_involving_node]}
        factors_list = set(itertools.chain(*self.factors.values()))
        product = factor_product(*factors_list)
        reduced_prod = product.reduce(evidence, inplace=False)
        reduced_prod.normalize()
        var_to_marg = (
            set(self.model.nodes()) - set(var) - set([state[0] for state in evidence])
        )
        marg_prod = reduced_prod.marginalize(var_to_marg, inplace=False)
        return marg_prod
    
# Defining a model

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

model = BayesianModel([("A", "J"), ("R", "J"), ("J", "Q"), ("J", "L"), ("G", "L")])
cpd_a = TabularCPD("A", 2, values=[[0.2], [0.8]])
cpd_r = TabularCPD("R", 2, values=[[0.4], [0.6]])
cpd_j = TabularCPD(
    "J",
    2,
    values=[[0.9, 0.6, 0.7, 0.1], [0.1, 0.4, 0.3, 0.9]],
    evidence=["A", "R"],
    evidence_card=[2, 2],
)
cpd_q = TabularCPD(
    "Q", 2, values=[[0.9, 0.2], [0.1, 0.8]], evidence=["J"], evidence_card=[2]
)
cpd_l = TabularCPD(
    "L",
    2,
    values=[[0.9, 0.45, 0.8, 0.1], [0.1, 0.55, 0.2, 0.9]],
    evidence=["J", "G"],
    evidence_card=[2, 2],
)
cpd_g = TabularCPD("G", 2, values=[[0.6], [0.4]])

model.add_cpds(cpd_a, cpd_r, cpd_j, cpd_q, cpd_l, cpd_g)

# Doing inference with our SimpleInference

infer = SimpleInference(model)

start = time.time()
a = infer.query(var=["A"], evidence=[("J", 0), ("R", 1)])
end = time.time()
print(f'Time for simple inference was {end-start} s.')

print(a)

# Comparing the results with Variable Elimination Algorithm

from pgmpy.inference import VariableElimination

infer = VariableElimination(model)

start = time.time()
result = infer.query(["A"], evidence={"J": 0, "R": 1})
end = time.time()
print(f'Time for simple inference was {end-start} s.')

print(result["A"])
