from HENMAP_chaos_model import Chaos
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
A = Chaos()
X = [0.12345, 0.23456, 0.34567]
last = []
for i in range(2000):
    X = A.runMaster(i, X)
    last.append(X)

last = np.array(last)
ax = plt.subplot(111, projection='3d')
ax.scatter(last[:, 0], last[:, 1], last[:, 2], c='y')

ax.set_zlabel('X3')
ax.set_ylabel('X2')
ax.set_xlabel('X1')
plt.show()