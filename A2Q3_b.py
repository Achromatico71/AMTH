import sympy as sp
from sympy.vector import CoordSys3D

N = CoordSys3D('N')
x, y = sp.symbols('x y')
f = N.y**2 * sp.cos(N.x - N.y)


f_x = sp.diff(f, N.x)
f_y = sp.diff(f, N.y)


u, v = sp.re(f), sp.im(f)
u_x = sp.diff(u, N.x)
u_y = sp.diff(u, N.y)
v_x = sp.diff(v, N.x)
v_y = sp.diff(v, N.y)

if u_x == v_y and u_y == -v_x:
    print("The function satisfies the Cauchy-Riemann equations.")
else:
    print("The function does not satisfy the Cauchy-Riemann equations.")


f_xx = sp.diff(f_x, N.x)
f_yy = sp.diff(f_y, N.y)
laplacian = f_xx + f_yy
print('The laplacian of the function is:', laplacian)

f_xy = sp.diff(f_x, N.y)
f_yx = sp.diff(f_y, N.x)
if f_xy == f_yx:
    print("The identity f_xy = f_yx is satisfied.")
else:
    print("The identity f_xy = f_yx is not satisfied.")
