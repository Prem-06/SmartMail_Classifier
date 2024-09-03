from numpy import exp
from random import *
import numpy as np
import matplotlib.pyplot as plt
# seed(1)
initial_value=20
def objective(x):
    return x**2.0

current_value=initial_value
current_obj=objective(current_value)
step=1
best_value=current_value
best_obj=current_obj
tolerance= {i:0 for i in range(0,1000)}
iteration=[i for i in range(1000)]
current=[0 for i in range(1000)]
for i in range(1000):
    potential_point=current_value+step*(randint(-100,100)/100)
    potential_obj=objective(potential_point)
    if potential_obj<current_obj:
        current_obj=potential_obj
        current_value=potential_point
    
    difference=potential_obj-current_obj

    tol=exp(-difference/(objective(initial_value)*float(i+1)))
    r=randint(0,100)/100
    tolerance[i]=tol
    if r<tol or difference<0:
        current_obj=potential_obj
        current_value=potential_point
    
    current[i]=current_obj
    iteration[i]=i

print("minimum value is")
print(current_obj)
print(current_value)
plt.scatter(iteration,current)
plt.show()


