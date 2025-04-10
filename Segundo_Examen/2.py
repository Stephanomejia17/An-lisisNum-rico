import numpy as np
import sympy as sp

from Biseccion import Biseccion
import matplotlib.pyplot as plt

f = lambda x: ((x + 4)*(x+2)*(x**2))*((x-2)**3)*(x-3)*(x-4)

u_x = np.linspace(-5, 4.5, 1000)

print(Biseccion(f, -5, 4.5, 1e-6))

plt.plot(u_x, f(u_x))
plt.axhline(0, color='black', linestyle='--')
plt.ylim(-5, 5)

plt.show()