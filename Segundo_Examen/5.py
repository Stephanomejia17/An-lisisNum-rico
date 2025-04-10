import numpy as np
import sympy as sp

from Secante import Secante 
import matplotlib.pyplot as plt

h = sp.symbols('h')
r = 2
L = 5
V = 8.5
tol = 1e-6

f = ((r**2 * sp.acos((r-h)/r) - (r - h * sp.sqrt(2*r*h - h**2))) * L )- V
a, b, res = Secante(f, h, 1, 1.2, tol)

print("h2: ", res[1])
print("El valor aproximado de h es: ", a)

f = sp.lambdify(h, f)

u_x = np.linspace(0, 10, 1000)


plt.plot(u_x, f(u_x))
plt.axhline(0, color='black', linestyle='--')

plt.show()