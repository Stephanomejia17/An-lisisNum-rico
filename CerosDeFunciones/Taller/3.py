import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from Biseccion import Biseccion

#Punto A
print("Punto a")
A = sp.symbols('A')
t = sp.symbols('t')

f = A*t*sp.exp(-t/3)
df = sp.diff(f, t)

despeje_t = sp.solve(df, t)[0]

f = A*t*sp.exp(-t/3) - 1
despeje_A = sp.solve(f, A)[0]

resuelto = despeje_A.subs(t, despeje_t)

print("Dosis: ", resuelto, "\nSe presenta a", despeje_t, "horas")

#Punto B
print("Punto B")
C= 1-0.25
print(resuelto)
f= lambda t: (resuelto)*t*np.exp(-t/3) - C
t= np.linspace(0, 15, 1000)
plt.plot(t, f(t))
plt.xlabel('t')
plt.ylabel('f(t)')
plt.axhline(0, color='black', linestyle='--')
plt.grid()
plt.show()

tiempo = Biseccion(f, 3, 15,1e-6)
print(tiempo)

#Punto C
print("Punto C")
C2= 0.25
A = (resuelto*.75)
g = lambda t : A*t*np.exp(-t/3) -C2
t= np.linspace(0, 15, 1000)
plt.plot(t, g(t))
plt.axhline(0, color='black', linestyle='--')
plt.grid()
plt.show()
tiempo3= Biseccion(g, 3, 15,1e-6)
print(tiempo3)