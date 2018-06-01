import matplotlib.pyplot as plt
import numpy as np
x1 = 0.1
x2 = 0.2
x3 = 0.3
x = []
y = []
for i in range(100):
    print(x1)
    x1 = 1.7 - x2**2 - 0.1 * x3
    x2 = x1 + 0.1
    x3 = x2

    x.append(x1)
    y.append(i)

plt.plot(y, x, '.')
plt.show()
