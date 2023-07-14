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
    plt.scatter(x_path[100:], y_path[100:], s=2, c="orange", linewidths=0)
    # plt.plot(x_path, y_path, "-o", linewidth=1, markersize=1, c="white")

    # Save the figure
    attractor_timestamp = time()
    plt.savefig(f"gallery/{attractor_timestamp}.png", dpi=1000)
    plt.show()
    plt.clf()  # Clear figure

# plt.plot(x_path, y_path, "-o", linewidth=1, markersize=1)
# plt.show()

parameters = (0.33956167635993895, -0.06812449881818972, [0.6774220710935643, -1.4444405245121392, -0.1508045386674719, 0.5110617417940468, -1.6586653780120901, -1.6663519861165867, 0.007814373212774228, -1.5432979564666196, 1.559470168857077, -0.2149094304937278, 1.4189893277212224, 1.5949577043189027])
draw(parameters)
