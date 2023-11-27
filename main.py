from pgmpy.models import BayesianNetwork
import time
import random 
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

start_time = time.time()

# model = BayesianNetwork([("A", "R"), ("A", "B"), ("A", "C"), ("A", "D"), ("A", "E")])

# Step 1: Define the model structure 
cancer_model = BayesianNetwork(
    [
        ("Pollution", "Cancer"),
        ("Smoker", "Cancer"),
        ("Cancer", "Xray"),
        ("Cancer", "Dyspnoea"),
    ]
)

end_time = time.time()

elapsed_time = end_time - start_time

print(f"Time taken to create the model: {elapsed_time:.6f} seconds")

start_time = time.time()

nx.draw(nx.DiGraph(cancer_model.edges()), with_labels=True)

end_time = time.time()

plt.show()

# Step 2: Define the CPDs
from pgmpy.factors.discrete import TabularCPD

cpd_poll = TabularCPD(variable="Pollution", variable_card=2, values=[[0.9], [0.1]])
cpd_smoke = TabularCPD(variable="Smoker", variable_card=2, values=[[0.3], [0.7]])
cpd_cancer = TabularCPD(
    variable="Cancer",
    variable_card=2,
    values=[[0.03, 0.05, 0.001, 0.02], [0.97, 0.95, 0.999, 0.98]],
    evidence=["Smoker", "Pollution"],
    evidence_card=[2, 2],
)
cpd_xray = TabularCPD(
    variable="Xray",
    variable_card=2,
    values=[[0.9, 0.2], [0.1, 0.8]],
    evidence=["Cancer"],
    evidence_card=[2],
)
cpd_dysp = TabularCPD(
    variable="Dyspnoea",
    variable_card=2,
    values=[[0.65, 0.3], [0.35, 0.7]],
    evidence=["Cancer"],
    evidence_card=[2],
)

# Step 3: Add the CPDs to the model. 

# Associating the parameters with the model structure.
cancer_model.add_cpds(cpd_poll, cpd_smoke, cpd_cancer, cpd_xray, cpd_dysp)

# Checking if the cpds are valid for the model.
cancer_model.check_model()

# 1. Create small world modular networks (incidence matrix)
# 2. Run inference algorithms from specification
# 3. Make sure the results align with the report.
# 4. Understand the algorithms.
# 5. Perform compositional analysis from paper 2.  

# 6. Might need to check variable elimination inference. Junction Tree, Loopy Belief propagation.

# THEN let's begin testing new inference algorithms and parallelization techniques.

# Let's create a small world modular network. 

