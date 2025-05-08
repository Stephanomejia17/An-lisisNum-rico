from MinimosCuadrados import MinimosCuadrados
import numpy as np
from Graficas import Graficas
import matplotlib.pyplot as plt


periodo = np.array([88, 224.7, 365.3, 4331.8, 10760.0, 30684.0, 60188.3, 90466.8])
distancia = np.array([36, 67.25, 93, 483.8, 887.97, 1764.5, 2791.05, 3653.9])

Graficas(periodo, distancia)
minimos = MinimosCuadrados(np.log(periodo), np.log(distancia))
u_x = np.linspace(min(np.log(periodo)), max(np.log(periodo)), 1000)
p = lambda x: minimos[0] + minimos[1]*x

# Verificando 
plt.plot(u_x, p(u_x))
plt.plot(np.log(periodo), np.log(distancia), 'or')
plt.show()

# Modelo no lineal
M = lambda x: np.exp(minimos[0]) * x**(minimos[1])
u_x = np.linspace(min(periodo), max(periodo), 1000)
plt.plot(periodo, distancia, 'or')
plt.plot(u_x, M(u_x))
plt.show()