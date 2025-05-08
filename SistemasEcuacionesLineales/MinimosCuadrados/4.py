import numpy as np
from Graficas import Graficas
from MinimosCuadrados import MinimosCuadrados
import matplotlib.pyplot as plt

peso = np.array([4,25,200,300,2000,5000,30000,50000,70000,450000,500000,3000000])

pulso = np.array([660, 670, 420, 300, 205, 120, 85, 70, 72, 38, 40, 48])

Graficas(peso, pulso)

minimos = MinimosCuadrados(np.log(peso), np.log(pulso))
p = lambda x: minimos[0] + minimos[1]*np.log(x)
M = lambda x: np.exp(minimos[0]) * x**(minimos[1])
u_x = np.linspace(min(peso), max(peso), 1000)

plt.plot(peso, pulso, 'or')
plt.plot(u_x, M(u_x))
plt.show()

print(M(2))