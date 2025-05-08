from Lagrange import Lagrange
import numpy as np
import matplotlib.pyplot as plt

x = [17, 19, 20, 22, 23, 25, 31, 32, 33, 36, 37, 38, 39, 41]

y = [19, 25, 32, 51, 57, 71, 141, 123, 187, 192, 205, 252, 248, 294]

res = Lagrange(x,y)

print("Evaluando: ", res[0](19), "\nPolinomio: ", res[1])


u_x = np.linspace(min(x), max(x), 100)
plt.plot(x, y, 'gp', label='Datos Observados')
plt.plot(u_x, res[0](u_x), 'r', label='Polinomio')
plt.legend()
plt.show()
