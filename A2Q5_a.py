import sympy as sp
x, y, z , t= sp.symbols('x y z t')
f = x**2 + 4*y**2 + z - 18
fx = f.diff(x)
fy = f.diff(y)
fz = f.diff(z)
t_plane = fx.subs({x:1, y:2, z:3})*(x-1) + fy.subs({x:1, y:2, z:3})*(y-2) + fz.subs({x:1, y:2, z:3})*(z-3)
print(t_plane)
# the parametric equation of normal line
n_x= 1 + t*fx.subs({x:1, y:2, z:1})
n_y= 2 + t*fy.subs({x:1, y:2, z:1})
n_z= 1 + t*fz.subs({x:1, y:2, z:1})
print('n_x(t) = ',n_x)
print('n_y(t) = ',n_y)
print('n_z(t) = ',n_z)
# the angle between tangent plane and xy plane
n = sp.sqrt(fx.subs({x:1, y:2, z:1})**2 + fy.subs({x:1, y:2, z:1})**2 + fz.subs({x:1, y:2, z:1})**2)
d = sp.sqrt(1**2 + 0**2 + 0**2)
theta = sp.acos(n/d)
print('theta = ',theta)