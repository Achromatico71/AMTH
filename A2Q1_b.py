import sympy as sp
from sympy.vector import CoordSys3D
n1 = sp.Matrix([3,-6,-2])
n2 = sp.Matrix([2,2,-5])
driect = n1.cross(n2)
C = CoordSys3D('C')
line = C.x*driect[0] + driect[1]*C.y + driect[2]*C.z
print('Line of intersection of the two planes in (b)')
print(line)
