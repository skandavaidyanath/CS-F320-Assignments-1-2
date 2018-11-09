import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mt
from math import log
from mpl_toolkits.mplot3d import Axes3D

# 2D case Circle
num_samples = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
r = 1

for sample_size in num_samples:
    plt.xlabel('x')
    plt.ylabel('y')
    plt.gca().set_aspect('equal', adjustable='box')
    valid_samples = 0
    x_valid, y_valid = [], []
    x_invalid, y_invalid = [], []
    for i in range(sample_size):
        x = np.random.uniform(low=-r, high=r)
        y = np.random.uniform(low=-r, high=r)
        if (x**2 + y**2) <= r**2:
            x_valid.append(x)
            y_valid.append(y)
            valid_samples = valid_samples + 1
        else:
            x_invalid.append(x)
            y_invalid.append(y)
    red = (1, 0, 0)
    plt.scatter(x_invalid, y_invalid, c=red, s=1)
    blue = (0, 0, 1)
    plt.scatter(x_valid, y_valid, c=blue, s=1)
    integral_estimate = 4*r*r*(valid_samples/sample_size)
    pi_estimate = integral_estimate/(r*r)
    plt.title('Sample Size {} Pi = {}'.format(sample_size, pi_estimate))
    plt.savefig("Q2A_images/Fig {}.png".format(round(log(sample_size, 10))))
    plt.close(1)
    print(pi_estimate)

# 3D Case Sphere
for sample_size in num_samples:
    valid_samples = 0
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect('equal', adjustable='box')
    x_valid, y_valid, z_valid = [], [], []
    x_invalid, y_invalid, z_invalid = [], [], []
    for i in range(sample_size):
        x = np.random.uniform(low=-r, high=r)
        y = np.random.uniform(low=-r, high=r)
        z = np.random.uniform(low=-r, high=r)
        if (x**2 + y**2 + z**2) <= r**2:
            x_valid.append(x)
            y_valid.append(y)
            z_valid.append(z)
            valid_samples = valid_samples + 1
        else:
            x_invalid.append(x)
            y_invalid.append(y)
            z_invalid.append(z)

    red = (1, 0, 0)
    # if we dont put alpha it is difficult to see the blue for larger sample sizes 
    ax.scatter(x_invalid, y_invalid, z_invalid, c=red, s=1, alpha=0.1)
    blue = (0, 0, 1)
    ax.scatter(x_valid, y_valid, z_valid, c=blue, s=1)

    integral_estimate = 8*r*r*r*(valid_samples/sample_size)
    pi_estimate = integral_estimate/((4/3)*r*r*r)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title('Sample Size {} Pi = {}'.format(sample_size, pi_estimate))
    plt.savefig("Q2B_images/Fig {}.png".format(round(log(sample_size, 10))))
    plt.close(1)
    print(pi_estimate)
