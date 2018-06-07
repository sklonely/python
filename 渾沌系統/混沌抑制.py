import numpy as np
import matplotlib.pyplot as plt

x1 = [-0.72]
x2 = [-0.64]

y1 = [-0.7201]
y2 = [-0.6401]

e1 = []
e2 = []

a = 0.9
b = -0.6013
c = 2
d = 0.5

for i in range(300):
    
    e1.append(x1[i] - y1[i])
    e2.append(x2[i] - y2[i])
    x1.append((x1[i]**2) - (x2[i]**2) + a * (x1[i]) + b * x2[i])
    y2.append(2 * x1[i] * x2[i] + c * x1[i] + d * x2[i])
    x1.append((y1[i]**2) - (y2[i]**2) + a * (y1[i]) + b * y2[i])
    y2.append(2 * y1[i] * y2[i] + c * y1[i] + d * y2[i])
"""
    e1[i] = x1[i] - y1[i]
    e2[i] = x2[i] - y2[i]

    x1[i + 1] = (x1[i]**2) - (x2[i]**2) + a * (x1[i]) + b * x2[i]
    x2[i + 1] = 2 * x1[i] * x2[i] + c * x1[i] + d * x2[i]

    y1[i + 1] = (y1[i]**2) - (y2[i]**2) + a * (y1[i]) + b * y2[i]
    y2[i + 1] = 2 * y1[i] * y2[i] + c * y1[i] + d * y2[i]
"""

plt.plot(x1, ".", y1, "o")
plt.xlabel('K')
plt.ylabel('X1 & Y1')
plt.show()
