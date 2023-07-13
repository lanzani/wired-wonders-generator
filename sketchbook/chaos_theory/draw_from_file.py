import math
import random
from time import time

from matplotlib import pyplot as plt


def draw(parameters):

    # Unpack the parameters
    x, y, a = parameters

    # lists to store the entire path
    x_path = [x]
    y_path = [y]

    for _ in range(10000):
        # Compute next point (using the quadratic map)
        x_new = a[0] + a[1] * x + a[2] * x * x + a[3] * y + a[4] * y * y + a[5] * x * y
        y_new = a[6] + a[7] * x + a[8] * x * x + a[9] * y + a[10] * y * y + a[11] * x * y


        # Update (x, y)
        x = x_new
        y = y_new

        # Save path
        x_path.append(x)
        y_path.append(y)

    # Plot the attractor
    plt.style.use("dark_background")

    plt.axis("off")
    plt.scatter(x_path[100:], y_path[100:], s=0.1, c="orange", linewidths=0)
    # plt.plot(x_path, y_path, "-o", linewidth=1, markersize=1, c="white")

    # Save the figure
    attractor_timestamp = time()
    plt.savefig(f"gallery/{attractor_timestamp}.png", dpi=1000)
    plt.show()
    plt.clf()  # Clear figure

# plt.plot(x_path, y_path, "-o", linewidth=1, markersize=1)
# plt.show()

parameters = (-0.29898047953560747, 0.25386507586153406, [1.0581923883183375, -0.8126521727342793, -0.4413979102313834, 0.505111988565992, 0.3102066341071499, -0.9607007939992322, -1.2599605613076537, -1.3052736169789845, 1.8385520969211342, -0.7291287968614948, 1.0794207160792157, 1.4894924780729881])

draw(parameters)
