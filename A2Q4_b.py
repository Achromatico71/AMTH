import numpy as np
import matplotlib.pyplot as plt
x = np.outer(np.linspace(1, 7, 100),np.ones(100))
y = x.copy().T
f1 = y**2 - 2*y*np.cos(x)
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot_surface(x, y, f1)
plt.title('f1 = y^2 - 2ycos(x)')
plt.show()
x = np.outer(np.linspace(0, 2*np.pi, 100),np.ones(100))
y = x.copy().T
f2 = np.abs(np.sin(x)*np.cos(y))
fig = plt.figure()
ax = plt.axes(projection ='3d')
ax.plot_surface(x, y, f2)
plt.title('f2 = |sin(x)cos(y)|')
plt.show()