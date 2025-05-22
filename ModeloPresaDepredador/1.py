import numpy as np
from Euler import euler
import matplotlib.pyplot as plt

# Funcion de ecuaciones Modelo Lotka-Volterra

def lotka(t, y):
    # y = es un arreglo y[0] = x1 y[1] = x2, .... , y[n-1] = xn
    # x1 = Presas
    # x2 = Depredadores
    x1 = y[0]
    x2 = y[1]
    k1 = 3 # natalidad de las presas 
    k2 = 3 # mortalidad de las presas
    k3 = 1 # natalidad de los depredadores
    k4 = 0.5 # mortalidad de los depredadores

    f1 = k1 * x1-k2*x1*x2# Ecuacion de las presas
    f2 = k3*x1*x2-k4*x2# Ecuacion de los depredadores
    return np.array([f1, f2])


tiempo, Modelo = euler(lotka, 0, 50, 0.01, np.array([0.1, 1]))
Presas = np.array(Modelo)[:, 0]
Depredadores = np.array(Modelo)[:, 1]

print("Presas: ", Presas)

# Graficar Presas vs Tiempo
# Graficar Depredadores vs Tiempo
# Graficar Presas vs Depredadores
plt.figure(figsize=(8,4))
plt.subplot(121)
plt.plot(tiempo, Presas, 'g', label='Presas')
plt.plot(tiempo, Depredadores, 'r', label='Depredadores')
plt.subplot(122)
plt.plot(Presas, Depredadores)
plt.xlabel('Presas')
plt.ylabel('Depredadores')

plt.show()
