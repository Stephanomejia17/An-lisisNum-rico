import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from Biseccion import Biseccion

#Punto_A
t = sp.symbols('t')
C = 1
A = sp.symbols('A')

h =t * sp.exp(-t / 3) #borre A

derivada_h = sp.diff(h, t)
print(f"Derivada: {derivada_h}")

f= sp.lambdify(t, derivada_h, 'numpy')
t = np.linspace(0, 10, 10000)

plt.axhline(0, color='black', linestyle='--')
plt.plot(t, f(t), label="f'(t)")
plt.grid()
plt.legend()
plt.show()

tiempo1=Biseccion(f,0,10,1e-6)
print(f"El tiempo de la máxima concentración es: {tiempo1[0]}")

A = lambda t: 1/(t * sp.exp(-t / 3))
valor_A = A(tiempo1[0])
print(f"La dosis de la máxima concentración es:{valor_A}")


#Punto_B
C= 0.25
f= lambda t: (valor_A)*t*np.exp(-t/3) -C
t= np.linspace(0, 15, 1000)
plt.plot(t, f(t))
plt.xlabel('t')
plt.ylabel('f(t)')
plt.axhline(0, color='black', linestyle='--')
plt.grid()
plt.show()

tiempo2 = Biseccion(f, 3, 15,1e-6)
print(f"Se debera aplicar la segunda dosis a las {tiempo2[0]} horas")


#Punto_C
A=np.exp(1)/3

C_total=lambda t: (A * t * np.exp(-t / 3)) + (0.75 * A) * (t - tiempo2[0]) * np.exp(-(t - tiempo2[0]) / 3)-0.25
u_x = np.linspace(15, 25, 1000)
Bisecc=Biseccion(C_total, 18, 25, 1e-6)
plt.plot(u_x, C_total(u_x))
plt.axhline(0, color='black', linestyle='--')
plt.show()
print("Se debera aplicar la tercera dosis a las ", Bisecc[0], "horas")
