from numpy import exp
from random import *
import numpy as np
import matplotlib.pyplot as plt

seed(1) # to keep random numbers consistent
n_iterations = 1000

def objective(x):
	return x**2.0      # objective function that we are trying to optimize

initial_val= 20         # user input for the unknown variable

step_size = 1          # some idea about the neighborhood for search

current_pt= initial_val # the current point
current_obj= objective(initial_val) # the objective function value at the current point


best_obj= current_obj # the best value of the objective found till now (initialized with the current objective)


# for post-processing of results like plotting etc.

tolerance= {i:0 for i in range(0,100)}
pt_plot= np.zeros((100,1))
iteration= np.zeros((100,1))

for i in range(0,100):

    potential_pt= current_pt + step_size * randint(-100, 100)/100 # potential new point
    potential_obj= objective(potential_pt) # the objective at that potential point

    if (potential_obj < best_obj): # if potential point's objective is better than the best value of objective found till now, updating the best objective and the best point till now
        
        best_pt= potential_pt
        best_obj= potential_obj
        
    difference_in_fitness= potential_obj - current_obj 
    
    tol= exp(-difference_in_fitness/objective(initial_val)*float(i+1))
    
    # if difference_in_fitness < 0, anyway moving toward that better potential point - "tol" has no role
    # if potential point is worse:  the "tol" is a fraction (0 to 1) -- for earlier iterations, value close to 1 and latter, value close to 0

    # check with other representation such square of iteration number, scaling w.r.t. initial value or initial objective
    
    tolerance[i]= tol

    r= randint(0, 100)/100

    if ((difference_in_fitness < 0) or (r < tol)): # if potential point's objective is better than the best value of objective found till now, the algorithm moves to that potential point as the new point
                                                   # else, in other case, may move to worse point if the random number (a fraction) is more or less than the "tol"
                                                   # so, in initial iterations, higher chance of selecting worse move (exploration) and latter, less chance of worse move (as the algorithm should have reached near to the optimal by then)
        current_obj= potential_obj
        current_pt= potential_pt

    pt_plot[i]= current_obj
    iteration[i]= i
    


plt.scatter(iteration, pt_plot, c ="blue")
plt.show()

# put x and y axes titles also
