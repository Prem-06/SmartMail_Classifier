import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def func(x, y):
    return x**3 + (y-1)**2 + np.sin(3*y+1.41)

# PSO setup
n_particles = 20
np.random.seed(100)
X = np.random.rand(2, n_particles)
V = np.random.randn(2, n_particles)
a = X
a_obj = func(X[0], X[1])
b = a[:, a_obj.argmin()]
b_obj = a_obj.min()

# Hyper-parameters
c1 = c2 = 0.1
w = 0.8

# To store particle positions over time for plotting
positions = [X.copy()]

def pso():
    global V, X, a, a_obj, b, b_obj
    r1, r2 = np.random.rand(2)
    
    V = w * V + c1 * r1 * (a - X) + c2 * r2 * (b.reshape(-1, 1) - X)
    X = X + V
    
    obj = func(X[0], X[1])
    a[:, (a_obj >= obj)] = X[:, (a_obj >= obj)]
    a_obj = np.array([a_obj, obj]).min(axis=0)
    
    b = a[:, a_obj.argmin()]
    b_obj = a_obj.min()
    
    # Store positions for plotting
    positions.append(X.copy())

# Run PSO for a specified number of iterations
for i in range(100):
    pso()

# Create a meshgrid for plotting the function surface
x = np.linspace(-1.5, 1.5, 100)
y = np.linspace(-1.5, 1.5, 100)
X_mesh, Y_mesh = np.meshgrid(x, y)
Z_mesh = func(X_mesh, Y_mesh)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X_mesh, Y_mesh, Z_mesh, cmap='viridis', alpha=0.7)

# Overlay particle trajectories
positions = np.array(positions)
for i in range(n_particles):
    ax.plot(positions[:, 0, i], positions[:, 1, i], func(positions[:, 0, i], positions[:, 1, i]), 'r-', marker='o')

# Mark the best position found
ax.scatter(b[0], b[1], func(b[0], b[1]), color='red', s=100, label="Best Position")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("Particle Swarm Optimization Trajectory")
plt.legend()
plt.show()
