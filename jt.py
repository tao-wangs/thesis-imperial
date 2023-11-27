from pgmpy.inference import VariableElimination, BeliefPropagation
from pgmpy.models import BayesianNetwork
import numpy as np
import pandas as pd
import time 

values = pd.DataFrame(np.random.randint(low=0, high=2, size=(1000, 5)),
                      columns=['A', 'B', 'C', 'D', 'E'])

model = BayesianNetwork([('A', 'B'), ('C', 'B'), ('C', 'D'), ('B', 'E')])
model.fit(values)
ve = VariableElimination(model)

start_time = time.time()
phi_query = ve.query(['A', 'B'])
end_time = time.time()
print(f'Time for Variable Elimination Algorithm: {end_time - start_time} s')
print(phi_query)

jt = BeliefPropagation(model)
start_time = time.time()
phi_query = jt.query(['A', 'B'])
end_time = time.time()
print(f'Time for Junction Tree Algorithm: {end_time - start_time} s')
print(phi_query)
