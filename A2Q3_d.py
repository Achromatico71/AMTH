import sympy as sp
from sympy.vector import *
import numpy as np
import matplotlib.pyplot as plt
C = CoordSys3D('C')
x, y = sp.symbols('x y')
r = 3*(C.x**3)*C.y
grad = gradient(r)
print(grad.subs({C.x: -1, C.y: 3/2}))
u = -1*C.i - (1/2)*C.j
u = u/u.magnitude()
print(u)
dd = grad.dot(u).subs({C.x: -1, C.y: 3/2})
print(dd)
x_va = np.linspace(-2, 0, 100)
y_va = np.linspace(0, 2, 100)
dd = sp.lambdify((x, y), dd)
X, Y = np.meshgrid(x_va, y_va)
plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(X, Y, dd(X, Y))
plt.show()