import sympy as sp
from sympy.vector import *
x, y = sp.symbols('x y')
f1 = 4*x**2 + y**2
fxx = sp.diff(f1,x,x)
fyy = sp.diff(f1,y,y)
fxy = sp.diff(f1,x,y)
if fxx*fyy - fxy**2 > 0:
    if fxx > 0:
        print('The function has a local minimum at:')
        print(sp.solve([sp.diff(f1,x),sp.diff(f1,y)]))
    else:
        print('The function has a local maximum at:')
        print(sp.solve([sp.diff(f1,x),sp.diff(f1,y)]))
else:
    print('The function has a saddle point')
    print(sp.solve([sp.diff(f1,x),sp.diff(f1,y)]))