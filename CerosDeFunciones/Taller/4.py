import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from Biseccion import Biseccion
from Falsa_Posicion import Falsa_posicion

h = 300
C = 1200
F = 0.8
D = 14
tol = 1e-6

f = lambda A: ((np.pi * ((h/np.cos(A))**2) * F)/(0.5 * np.pi * D**2 * (1 + np.sin(A) - 0.5 * np.cos(A)))) - C
#Gráfica

A = np.linspace(0, np.pi, 100)
plt.figure(figsize=(10,6))
plt.axhline(0, color='black', linewidth=1)
plt.ylim(-100,100)
plt.plot(A, f(A), label='f(A)', color='blue')
plt.legend()
plt.title('Gráfica de la Función')
plt.xlabel('t')
plt.ylabel('Valor de la función')
plt.grid()
plt.show()

A = sp.symbols('A')

f2 = ((sp.pi * ((h/sp.cos(A))**2) * F)/(0.5 * sp.pi * D**2 * (1 + sp.sin(A) - 0.5 * sp.cos(A)))) - C


bisecc = Biseccion(f,0,0.5,tol)
falsa = Falsa_posicion(f, 0, 0.5, tol)


print("Biseccion: ", np.degrees(bisecc[0]))
print("Falsa Posicion: ", np.degrees(falsa[0]))

print(f"El ángulo A del anillo corresponde a {np.degrees(bisecc[0])}")