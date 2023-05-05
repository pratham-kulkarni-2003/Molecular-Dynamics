import numpy as np
import matplotlib.pyplot as plt

# Initialize position and velocity of particles
np.random.seed(0)
pos = np.random.rand(3, 1000)*1.7
vel = np.zeros((3, 1000))

# Constants
dt = 0.001
n_steps = 10000
sigma = 1
epsilon = 1
r_cutoff = 2.5*sigma
box_size = 1.7

# Initialize neighbour list
neighbour_list = []
for i in range(1000):
    neighbours = []
    for j in range(1000):
        if i != j:
            r = np.sqrt(np.sum((pos[:, i] - pos[:, j])**2))
            if r < r_cutoff:
                neighbours.append(j)
    neighbour_list.append(neighbours)

# Velocity Verlet algorithm
for step in range(n_steps):
    # Compute forces
    force = np.zeros((3, 1000))
    for i in range(1000):
        for j in neighbour_list[i]:
            r = pos[:, j] - pos[:, i]
            r_sq = np.sum(r**2)
            r_norm = np.sqrt(r_sq)
            force_ij = 24*epsilon*(2*(sigma**12/r_sq**7) - (sigma**6/r_sq**4))*r/r_norm
            force[:, i] += force_ij
            force[:, j] -= force_ij
    # Update positions
    pos += vel*dt + 0.5*force*dt**2
    #Check for wall crossings and handle them
    for i in range(1000):
        for j in range(3):
            if pos[j,i] > box_size:
                pos[j,i] = pos[j,i]-box_size
                if pos[j,i] < 0:
                    pos[j,i] = pos[j,i]+box_size
    # update neighbour list
    for i in range(1000):
        for j in neighbour_list[i]:
            r = np.sqrt(np.sum((pos[:, i] - pos[:, j])**2))
            if r > r_cutoff:
                neighbour_list[i].remove(j)
# Plot velocity of particles
plt.hist(np.linalg.norm(vel, axis=0), bins=50)
plt.xlabel('Velocity')
plt.ylabel('Count')
plt.show()