from numpy.random import randint
from numpy.random import rand
from numpy.random import seed
# to keep the random numbers consistent for a set of run, one may use seed()
#seed(1) - the number inside this bracket is to remain same
seed(33)

# objective function
def objective(x):
	return x[0]**2.0 + x[1]**3.0

# define range for input
x_bounds = [[-10.0, 5.0], [2.0, 10.0]]

# define the total iterations [ideally stop the iteration when convergence happens]
n_iteration = 1000


# bits per variable [more the value, more intensive and more efficient]
n_bits = 16                      # total length of the bit string = 16 x 2 = 32


# define the agent size (no. of agents), larger the size: more quickly the solution can be found, but, more time-consuming each iteration/generation would be
n_agents = 10
# crossover rate
rate_crossover = 0.9

# mutation rate
rate_mutation = 1.0 / (float(n_bits) * len(x_bounds))  # inverse of total number of bits in the bitstrings

# Tournament selection
# draw k candidates randomly from the entire population of the agents (at the present generation/iteration)
# select member from the group (k candidates) as per their fitness
# most typical value of k is 3, that's why first one randomly picked up and then comparing with two more such


def selection(pop_agents, fitness_function_value):
	
	selected_frompop = randint(len(pop_agents))  # randomly select one from the entire population of agents 

	for i in randint(0, len(pop_agents), 2): # two more randomly picked up
    
        # checking which one has the lowest value of the score (fitness/objective function)
        
		if fitness_function_value[i] > fitness_function_value[selected_frompop]:
			selected_frompop = i

    # selected_frompop contain index of maximum of fitness_function_value 

	return pop_agents[selected_frompop]

# Crossover
# at every iteration/generation,
# from two agents (selected by any technqiue, as above),
# crossover function gives two new members (as per the specific crossover strategy)

def crossover(a1, a2, rate_crossover):

	c1, c2 = a1.copy(), a2.copy()   # the current agents are copied

	if rand() < rate_crossover:   # any random fraction - if that is lesser than the rate of crossover, following operations would be carried out
                                  # so, for k=0.9, 90 % chance of the following crossover operations to take place

		pt = randint(1, len(a1)-2)  # selecting the crossover point randomly anywhere in the string [there may be other strategies too]

		c1 = a1[:pt] + a2[pt:]
		c2 = a2[:pt] + a1[pt:]

	return [c1, c2]


# Mutation


def mutation(bitstring, rate_mutation):

	for i in range(len(bitstring)):
		if rand() < rate_mutation: # any random fraction - if that is lesser than the rate of mutation, mutation happens
			
			bitstring[i] = 1 - bitstring[i]   # 0 becomes 1 and 1 becomes 0
# Converting/Decoding binary encoding to real number as per decimal system
       
def convert(bounds, n_bits, bitstring):
	
	decoded = list()
	largest = 2**n_bits # the largest possible value (converting binary to real number in decimal)
             
	for i in range(len(bounds)):
		
		k_start, k_end = i * n_bits, (i * n_bits)+n_bits
		substring_pervar = bitstring[k_start:k_end]   # the substring corresponding to each variable
# next, converting the bitstring to character string and then to value (as per the lower bound-upper bound scaling)
		
		chars = ''.join([str(s) for s in substring_pervar])
		
		integer = int(chars, 2)
		value = bounds[i][0] + (integer/largest) * (bounds[i][1] - bounds[i][0])
		
		decoded.append(value)  # the values corresponding to the bit string is stored in the list and returned back to where from it has been called

	return decoded

# genetic algorithm - main part, calling the different operators, as necessary

def ga(objective, x_bounds, n_bits, n_iteration, n_agents, rate_crossover, rate_mutation):
	
	pop_agents = [randint(0, 2, n_bits*len(x_bounds)).tolist() for _ in range(n_agents)]   # initializing all the agents with random bitstring (binary 0 or 1)
	
	best, best_obj = 0, objective(convert(x_bounds, n_bits, pop_agents[0]))  # initializing the best evaluated objective function (thus far) with the first agent [folllowing the conversion to decimal number]
	
	for k in range(n_iteration):     # for the specified number of iterations, ideally, it should be made to stop when convergence has been achieved
		
		decoded = [convert(x_bounds, n_bits, p) for p in pop_agents]
		
		fitness_function_value = [objective(d) for d in decoded] # for all the decoded values (corresponding to the bit strings of the agents), the fitness is being evaluated
		
		for i in range(n_agents):           # for all the agents

			if float(fitness_function_value[i]) > float(best_obj): # if the value has been better than the best evaluated objective (fitness function) so far

				best, best_realvalue, best_obj = pop_agents[i], decoded[i], fitness_function_value[i]  # the value of best evaluated objective is updated and the "best" is that agent (so far)


				# this specific best evaluated value, the agent's value (in decimal) and the iteration/generation number and etc can be printed
                # to see the progress of the calculations    
                
		# now for calculating new agents: selection, crossover, mutation
        
		selected_agents = [selection(pop_agents, fitness_function_value) for _ in range(n_agents)] # total number of selected agents = total number of agents (but how are they selected? as per tournament or other selection schemes)
		
		new_agents = list()

		for i in range(0, n_agents, 2):	 
			
			a1, a2 = selected_agents[i], selected_agents[i+1] # taking two agents at a time for the following operations and...... the same will proceed for all the selected agents
            
			for c in crossover(a1, a2, rate_crossover):
				
				mutation(c, rate_mutation)
				
				new_agents.append(c)   # storing into the list         
            
		
		pop_agents = new_agents # replacing the old agents with the new ones

	return [best, best_realvalue, best_obj]


best, best_realvalue, best_obj = ga(objective, x_bounds, n_bits, n_iteration, n_agents, rate_crossover, rate_mutation)


print('f(%s) = %f' % (best_realvalue, best_obj))