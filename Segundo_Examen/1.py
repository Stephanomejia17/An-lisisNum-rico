import numpy as np
import sympy as sp
from Newton import Newton

import matplotlib.pyplot as plt

x = sp.symbols('x')

f = x**4 - 17*x**2 + 60
df = sp.diff(f, x)
print("derivada: ", df)

a, b, rpta = Newton(f, x, 2, 1e-6)

print("x2 : ", rpta[1])
print("p(x2): ", f.evalf(subs={x:rpta[1]}))
print("p'(x2): ", df.evalf(subs={x:rpta[1]}))

print("la raiz es igual a: ", a)

u_x = np.linspace(0,5,1000)

f = sp.lambdify(x, f)
plt.plot(u_x, f(u_x))
plt.axhline(0, color='black', linestyle='--')

plt.show()

