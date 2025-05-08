from Lagrange import Lagrange

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

anho = np.array([1940, 1945, 1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990])
pezAzul = np.array([15000, 150000, 250000, 275000, 270000, 280000, 290000, 650000, 1200000, 1500000, 2750000])

x = sp.symbols('x')
u_x = np.linspace(min(anho), max(anho), 1000)
P = sp.lambdify(x, Lagrange(anho, pezAzul)[1])

plt.plot(anho, pezAzul, 'or', label='Data')
plt.plot(u_x, P(u_x), label='Polinomio')
plt.legend()
plt.show()

plt.figure(figsize=(12,12), dpi=100)


""""""

# grafica x, y
plt.subplot(3,3,1)
plt.plot(anho, pezAzul, 'or', label='x, y')
plt.legend()
# grafica x sqr y
plt.subplot(3,3,2)
plt.plot(anho, np.sqrt(pezAzul), 'or', label='raiz y, x')
plt.legend()
# Grafica x, 1/y
plt.subplot(3,3,3)
plt.plot(anho, 1/pezAzul, 'or', label='x, 1/y')
plt.legend()
# Grafica x**2, y
plt.subplot(3,3,4)
plt.plot(anho**2, pezAzul, 'or', label='x**2, y')
plt.legend()
#Grafica x**3, y
plt.subplot(3,3,5)
plt.plot(anho**3, pezAzul, 'or', label='x**3, y')
plt.legend()
# Grafica Log x, y
plt.subplot(3,3,6)
plt.plot(np.log(anho), pezAzul, 'or', label='Log(x), y')
plt.legend()
# Grafica x, Log y
plt.subplot(3,3,7)
plt.plot(anho, np.log(pezAzul), 'or', label='x, Log(y)')
plt.legend()
# Grafica sqr x, y
plt.subplot(3,3,8)
plt.plot(np.sqrt(anho), pezAzul, 'or', label='raiz x, y')
plt.legend()
# Grafica Log x, Log y
plt.subplot(3,3,9)
plt.plot(np.log(anho), np.log(pezAzul), 'or', label='Log x, Log y')
plt.legend()
plt.show()