import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.symbols('t')
r_t = sp.Matrix([sp.exp(t), sp.exp(t) * sp.cos(t), sp.exp(t) * sp.sin(t)])

r_1 = sp.Matrix(r_t.diff(t))
r_2 = sp.Matrix(r_1.diff(t))
r_3 = sp.Matrix(r_2.diff(t))

v_c_a = sp.Matrix(r_1.cross(r_2))

Tau = r_1/ r_1.norm()
print("Tangent:")
print(Tau)

Binormal = v_c_a / v_c_a.norm() 
print("Binormal:")
print(Binormal)

Normal = Binormal.cross(Tau)
print("Normal:")
print(Normal)

kappa = v_c_a.norm() / r_1.norm()**3
print("Curvature:")
print(kappa)

Torsion = v_c_a.cross(r_3) / v_c_a.norm()
print("Torsion:")
print(Torsion)

tt = np.linspace(0, 2*np.pi, 100)
kappa = sp.lambdify(t, kappa, 'numpy')
plt.plot(tt, kappa(tt))
plt.xlabel('t')
plt.ylabel('kappa')
plt.title('Curvature')
plt.show()