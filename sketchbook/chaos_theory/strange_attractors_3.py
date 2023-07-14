import math
import random
from time import time

import pandas as pd
from matplotlib import pyplot as plt
import datashader as ds
from datashader import transfer_functions as tf
from numba import jit


@jit(nopython=True)
def draw(parameters, attractor_timestamp):
    # Unpack the parameters
    x, y, a = parameters

    # lists to store the entire path
    x_path = [x]
    y_path = [y]

    for _ in range(10000000):
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
    # plt.style.use("dark_background")
    #
    # plt.axis("off")
    # plt.scatter(x_path[100:], y_path[100:], s=0.1, c="#fff", linewidths=0)
    # # plt.plot(x_path, y_path, "-o", linewidth=1, markersize=1, c="white")
    #
    # # Save the figure
    #
    # plt.savefig(f"gallery/{attractor_timestamp}.png", dpi=300)
    # plt.show()
    # plt.clf()  # Clear figure

    return x_path, y_path


# plt.plot(x_path, y_path, "-o", linewidth=1, markersize=1)
# plt.show()

# parameters = (-0.22924158448035303, 0.13882089893721417,
#               [-0.6871787065237953, 1.7072846610057328, 1.1008983717375957, -0.8628120210914716, 0.22069880500938766,
#                -0.2652412644557778, 0.3301968368190553, 0.9934424758848981, 0.6049467172631928, 0.5802788345840271,
#                0.7676033557740749, 1.5966081380952213])

parameters = (0.33956167635993895, -0.06812449881818972,
              [0.6774220710935643, -1.4444405245121392, -0.1508045386674719, 0.5110617417940468, -1.6586653780120901,
               -1.6663519861165867, 0.007814373212774228, -1.5432979564666196, 1.559470168857077, -0.2149094304937278,
               1.4189893277212224, 1.5949577043189027])

attractor_timestamp = time()
x, y = draw(parameters, attractor_timestamp)

df = pd.DataFrame(dict(x=x, y=y))

cvs = ds.Canvas(plot_width=1920, plot_height=1440)
agg = cvs.points(df, 'x', 'y')
print(agg.values[190:195, 190:195], "\n")

ds.transfer_functions.Image.border = 0



img = tf.shade(agg, cmap=["white", "black"])

img.to_pil().save("gallery/strange_attractor_datashader_1.png")
