import numpy as np
import sympy as sp

from Biseccion import Biseccion
import matplotlib.pyplot as plt

f = lambda x: np.log(x**2 + 1) - np.exp(0.4*x)*np.cos(np.pi * x)

print("El único cero negativo es: ", Biseccion(f, -1, 0, 1e-6))
print("Uno de los ceros mas pequeños es: ", Biseccion(f, 0, 1, 1e-6))

u_x = np.linspace(-0.5, 100, 1000)

plt.plot(u_x, f(u_x))
plt.axhline(0, color='black', linestyle='--')
plt.xlim(-1, 1)
plt.ylim(-1,1)
plt.show()
