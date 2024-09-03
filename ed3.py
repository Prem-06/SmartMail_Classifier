import numpy as np
import matplotlib.pyplot as plt
def func(x,y):
    return x**3 + (y-1)**2 + np.sin(3*y+1.41)
n_particles = 20
np.random.seed(100)

X = np.random.rand(2, n_particles)
V = np.random.randn(2, n_particles)
# the location of the particles on x-y plane (random): an array of the given shape with random samples from a uniform distribution over [0, 1)
# the velocity : random floats sampled from a univariate “normal” (Gaussian) distribution of mean 0 and variance 1
a = X # X 
a_obj = func(X[0], X[1]) # the objective function value corresponding to each element of a
check= a_obj
b = a[:, a_obj.argmin()] # that particular element of "a" (from among all the "a"s of all particles) which corresponds to the least value of objective function 
b_obj = a_obj.min() # the value of that objective function at that point

# Hyper-parameter of the algorithm
c1 = c2 = 0.1
w = 0.8


def pso():

    global V, X, a, a_obj, b, b_obj
    # Update params
    r1, r2 = np.random.rand(2)
    
    V = w * V + c1*r1*(a - X) + c2*r2*(b.reshape(-1,1)-X)  # this is how the algorithm updates X of each particle 
    X = X + V
    
    obj = func(X[0], X[1])

    a[:, (a_obj >= obj)] = X[:, (a_obj >= obj)] # best of X found till now by a specific particle, so, for better points, a gets updated with that point (X), comparing earlier iteration's a_obj with current's obj
    a_obj = np.array([a_obj, obj]).min(axis=0) # the minimum of objectives for each particle

    b = a[:, a_obj.argmin()] # best of the points explored by any of the particles
    b_obj = a_obj.min()
    


for i in range(0,1000):
    pso()

# print(X)
# print(b)
# print(b_obj)
# ideally there should be stopping criterion

# further post-processing like plots etc.



