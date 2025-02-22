import sympy as sp
x, y, z, theta = sp.symbols('x y z theta')
x = sp.cos(theta)
y = sp.sin(theta)
z = sp.tan(theta)
f = sp.sqrt(x**2 + y**2 + z**2)
f_theta = sp.diff(f, theta)
print(f_theta.subs(theta, sp.pi/4))