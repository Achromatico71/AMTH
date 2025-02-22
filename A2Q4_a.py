import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-10, 10, 100)
Y = np.linspace(-10, 10, 100)
Z = np.linspace(-10, 10, 100)
[X, Y] = np.meshgrid(X, Y)
f1 = 4*X**2 + Y**2
levels = [1, 2, 4, 9, 16, 25, 36]
fig = plt.figure()
plt.contourf(X, Y, f1, levels)
plt.colorbar()
plt.show()