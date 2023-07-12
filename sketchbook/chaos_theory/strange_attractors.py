import random
from matplotlib import pyplot as plt

found = False

while not found:
    converging = False

    # Random starting point
    x = random.uniform(-0.5, 0.5)
    y = random.uniform(-0.5, 0.5)

    # Random parameter vector
    a = [random.uniform(-2, 2) for _ in range(12)]

    # lists to store the entire path
    x_path = [x]
    y_path = [y]

    for _ in range(10000):
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

        # Update (x, y)
        x = x_new
        y = y_new

        # Save path
        x_path.append(x)
        y_path.append(y)

    if not converging:
        found = True

plt.scatter(x_path, y_path, s=0.1)
plt.show()