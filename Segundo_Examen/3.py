import numpy as np
import sympy as sp

from Biseccion import Biseccion
import matplotlib.pyplot as plt

f = lambda x: (x+3)*(x+1)*(x**2)*((x-1)**3)*(x-2)*(x-4)

u_x = np.linspace(-3.5, 4.5, 1000)

print(Biseccion(f, -3.5, 4.5, 1e-6))

plt.plot(u_x, f(u_x))
plt.axhline(0, color='black', linestyle='--')
plt.ylim(-10,10)

plt.show()