
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from Biseccion import Biseccion


Lct = 0.088
tol = 1e-6
f = lambda t: - np.sqrt((1/2) * Lct) + np.exp(-(1/2)*t) * np.arccosh(np.exp((1/2)*t))

#Grafica
t = np.linspace(0, 10, 1000)
plt.figure(figsize=(10,6))
plt.axhline(0, color='black', linewidth=1)
plt.plot(t, f(t), label='f(T)', color='blue')
plt.legend()
plt.title('Gráfica de la Función')
plt.xlabel('t')
plt.ylabel('Valor de la función')
plt.grid()
plt.show()


t = sp.symbols('t')
f1 = sp.sqrt((1/2) * Lct) - sp.exp(-(1/2)*t) * sp.acosh(sp.exp((1/2)*t))

tiempo=Biseccion(f, 1, 10, tol)
print(f"El valor de t es {tiempo[0]}")