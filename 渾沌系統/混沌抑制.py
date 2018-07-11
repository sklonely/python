import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

x1 = [-0.72]
x2 = [-0.64]

e1 = []
uk = []

A = -0.3
a = 0.9
b = -0.6013
c = 2
d = 0.5
t = []
for i in range(100):
    if (i > 50):
        uk.append(-((x1[i]**2) - (x2[i]**2) + a * (x1[i]) + b * (x2[i]) + A * x1[i]))
    else:
        uk.append(0)

    x1.append((x1[i]**2) - (x2[i]**2) + a * (x1[i]) + b * x2[i] + uk[i])
    x2.append(2 * x1[i] * x2[i] + c * x1[i] + d * x2[i])
    t.append(i)

plt.figure()
plt.subplot(111)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.plot(x1[0:50], x2[0:50], ".", x1[51:100], x2[51:100], ".")
plt.xlabel("x1", fontsize=24)
plt.ylabel("x2", fontsize=24)

plt.show()
