import sympy as sp
import numpy as np 
import matplotlib.pyplot as plt
t = sp.Symbol('t')
r = sp.Matrix([5*sp.cos(t),4*sp.sin(t)])
v = sp.diff(r,t)
v = sp.ImmutableDenseMatrix(v)
print('Tangent vector at point t = pi/4')
print(v.subs(t,sp.pi/4))
print('Tangent vector at point t = pi')
print(v.subs(t,sp.pi))
tt = np.linspace(-np.pi,np.pi, 100)
r_x = sp.lambdify([t],r[0])
r_y = sp.lambdify([t],r[1])
v_x = sp.lambdify([t],v[0])
v_y = sp.lambdify([t],v[1])
plt.plot(r_x(tt),r_y(tt))
plt.title('Plot of Curve C')
plt.figure
plt.quiver([0,0],[0,0],r_x([np.pi,np.pi/4]),r_y([np.pi,np.pi/4]), angles='xy', scale_units='xy', scale=1 , color = ['r','b'])
plt.quiver(r_x([np.pi,np.pi/4]),r_y([np.pi,np.pi/4]),v_x([np.pi,np.pi/4]),v_y([np.pi,np.pi/4]), angles='xy', scale_units='xy', scale=1, color = ['r','b'])
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.show()