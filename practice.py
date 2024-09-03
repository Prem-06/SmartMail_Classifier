import numpy as np
from numpy.random import randint,rand,seed
seed(33)
n_agents=10
x_bound=[[-10,5],[-4,10]]
n_bits=16
n_iteration=1000
rate_crossover=0.9
rate_mutation=1/(float(n_bits)*float(len(x_bound)))
def objective(x):
    return x[0]**2.0 + x[1]**3.0

def selection(solutions,fitness_value):
    selected_index=randint(0,len(solutions))

    for i in randint(0,len(solutions),2):
        if fitness_value[i]>fitness_value[selected_index]:
            selected_index=i
    
    return solutions[selected_index]


def convert(solution,n_bits,x_bound):
    decoded=[]
    largest=2**n_bits
    for i in range(len(x_bound)):
        start,end=i*n_bits,(i*n_bits)+n_bits
        sol=solution[start:end]
        bitstring=""
        for s in sol:
            bitstring=bitstring+str(s)
        int_value=int(bitstring,2)
        int_value=x_bound[i][0]+(int_value/largest)*(x_bound[i][1]-x_bound[i][0])
        decoded.append(int_value)
    return decoded

def crossover(a1,a2,rate_crossover):
    c1=a1.copy()
    c2=a2.copy()
    
    if rand()<rate_crossover:
        pt=randint(1,len(a1)-2)
        c1 = np.concatenate((a1[:pt], a2[pt:])) 
        c2 = np.concatenate((a2[:pt], a1[pt:]))
    
    return [c1,c2]

def mutation(solution,rate_mutation):
    for i in range(len(solution)):
        if rand()<rate_mutation:
            solution[i]=1-solution[i]
    

def gentic_algorithum(objective,n_agents,x_bound,n_bits,n_iteration,rate_crossover,rate_mutation):
    
    solutions=[]
    for i in range(n_agents):
        solution=randint(0,2,n_bits*len(x_bound))
        solutions.append(solution)
    
    best,best_obj=0,objective(convert(solutions[0],n_bits,x_bound))
    for itr in range(n_iteration):
    #   fitness_value store objective value of each solution 
    #   decoded_val store the decimal value of solution
      fitness_value=[]
      decoded_val=[]
      for s in solutions:
         decoded=convert(s,n_bits,x_bound)
         decoded_val.append(decoded)
         obj=objective(decoded)
         fitness_value.append(obj)
    
      for i in range(n_agents):
        if float(fitness_value[i])>float(best_obj):
            best_obj=fitness_value[i]
            best=solutions[i]
            best_realvalue=decoded_val[i]
      selected=[]
      for i in range(n_agents):
        selected.append(selection(solutions,fitness_value))
    
     
      new_agents=list()
    
      for i in range(0,n_agents,2):
        a1,a2=selected[i],selected[i+1]

        for c in crossover(a1,a2,rate_crossover):
            mutation(c,rate_mutation)
            new_agents.append(c)
    
      solutions=new_agents

    return [best,best_realvalue,best_obj]

    
best,bestreal_value,best_obj=gentic_algorithum(objective,n_agents,x_bound,n_bits,n_iteration,rate_crossover,rate_mutation)

print(best,bestreal_value,best_obj)


