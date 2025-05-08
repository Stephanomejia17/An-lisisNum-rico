from Lagrange import Lagrange

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from MinimosCuadrados import MinimosCuadrados
from Graficas import Graficas

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

Graficas(anho,pezAzul)

mnmcs = MinimosCuadrados(anho, np.log(pezAzul))
p = lambda x: mnmcs[0] + mnmcs[1]*x
print(mnmcs, p)

# Graficar los datos en la escala(escogida) y el modelo no lineal determinado por una regresión de minimos cuadrados
u_x = np.linspace(min(anho), max(anho), 1000)
plt.scatter(anho, np.log(pezAzul))
plt.plot(u_x, p(u_x), 'r')
plt.show()

# a partir de Y=a_0 + a_1 * x, dependiendo de la escala, en este caso Log(x), y el modelo no lineal es: 
# M = a_0 + a_1 Log(x)
u_x = np.linspace(min(anho), max(anho), 1000)
M = lambda x: np.exp(mnmcs[0]) * np.exp(mnmcs[1]*x)

plt.plot(anho, pezAzul, 'or', label='Datos')
plt.plot(u_x, M(u_x))
plt.legend()
plt.show()