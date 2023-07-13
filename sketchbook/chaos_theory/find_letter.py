import math
import random
import time

import cv2
import easyocr
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

attractors_to_save = 1
found = 0

while found < attractors_to_save:

    # Random starting point
    x = random.uniform(-0.5, 0.5)
    y = random.uniform(-0.5, 0.5)

    # Random alternative starting point nearby
    xe = x + random.uniform(-0.5, 0.5) / 1000
    ye = y + random.uniform(-0.5, 0.5) / 1000

    # Distance between the two points
    dx = xe - x
    dy = ye - y
    d0 = math.sqrt(dx * dx + dy * dy)

    # Random parameter vector
    a = [random.uniform(-2, 2) for _ in range(12)]

    # lists to store the entire path
    x_path = [x]
    y_path = [y]

    # Flag to check if the path converges to a single point and lyapunov exponent
    converging = False
    lyapunov = 0

    for i in range(10000):
        # Compute next point (using the quadratic map)
        x_new = a[0] + a[1] * x + a[2] * x * x + a[3] * y + a[4] * y * y + a[5] * x * y
        y_new = a[6] + a[7] * x + a[8] * x * x + a[9] * y + a[10] * y * y + a[11] * x * y

        # Check if converge to infinity
        if x_new > 1e10 or x_new < -1e10 or y_new > 1e10 or y_new < -1e10:
            converging = True
            break

        # Check if converge to a single point
        if abs(x_new - x) < 1e-10 and abs(y_new - y) < 1e-10:
            converging = True
            break

        # Check for chaotic behavior (wait for 1000 iterations)
        if i > 1000:
            # Compute next alternative point (using the quadratic map)
            xe_new = a[0] + a[1] * xe + a[2] * xe * xe + a[3] * ye + a[4] * ye * ye + a[5] * xe * ye
            ye_new = a[6] + a[7] * xe + a[8] * xe * xe + a[9] * ye + a[10] * ye * ye + a[11] * xe * ye

            # Compute distance between the two points
            dx = xe_new - x_new
            dy = ye_new - y_new
            d = math.sqrt(dx * dx + dy * dy)

            # Lyapunov exponent
            lyapunov += math.log(abs(d / d0))

            # Rescale the alternative point
            # Random alternative starting point nearby
            xe = x_new + d0 * dx/d
            ye = y_new + d0 * dy/d


        # Update (x, y)
        x = x_new
        y = y_new

        # Save path
        x_path.append(x)
        y_path.append(y)

    # If chaotic behavior is found
    if not converging and lyapunov >= 10: # if lyapunov >= 10, then the path is chaotic
        # found += 1

        print(f"Found attractor with lyapunov exponent: {lyapunov}")
        plt.clf()
        plt.scatter(x_path, y_path, s=0.1)
        plt.axis("off")

        # Convert plt to cv2 image
        fig = plt.gcf()
        fig.canvas.draw()
        w, h = fig.canvas.get_width_height()
        img = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
        img = img.reshape((h, w, 3))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imwrite(f"attractor_{found}.png", img)


        reader = easyocr.Reader(['en'])
        result = reader.readtext(img)
        print(result)

        # if found end the cycle
        if len(result) > 0 and result[0][1] == "F":
            found = attractors_to_save



# plt.plot(x_path, y_path, "-o", linewidth=1, markersize=1)
# plt.show()
