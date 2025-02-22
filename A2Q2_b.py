import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
t, s= sp.symbols('t s')
r_t = sp.Matrix([sp.cos(t),sp.sin(t),t])
v_t = sp.Matrix(r_t.diff(t))
v_norm = sp.sqrt(v_t.dot(v_t))
s_arc = sp.integrate(v_norm, (t, 0, t))
t_s = sp.solve(s_arc- s, t)[0]
r_s = r_t.subs(t, t_s)
r_s= sp.simplify(r_s)
r_s = sp.lambdify(s, r_s)
print("Bug's final co-ordinate")
print(r_s(10))
s_range = np.linspace(0, 10, 100)
r_s_range = np.array([r_s(s_val) for s_val in s_range])
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(r_s_range[:,0], r_s_range[:,1], r_s_range[:,2])
plt.title('Walking of the bug along the curve')
plt.show()