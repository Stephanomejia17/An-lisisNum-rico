import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Biseccion import Biseccion
from Falsa_Posicion import Falsa_posicion
from Newton import Newton
from Secante import Secante

C = lambda s: s**3 + 12.5*s**2 + 50.5 * s + 66
N = lambda s: s**4 + 19*s**3 + 122*s**2 + 296*s + 192

roots = []
x0 = -10
x1 = 10
tol = 1e-6


#Graficar funciones y sus ceros
s = np.linspace(-10, 2, 1000)
plt.figure(figsize=(10,6))
plt.ylim(-30,30)
plt.axhline(0, color='black', linewidth=1)
plt.plot(s, C(s), label='C(s)', color='blue')
plt.plot(s, N(s), label='N(s)', color='red')
plt.legend()
plt.title('Gráfica de las funciones C(s) y N(s)')
plt.xlabel('s')
plt.ylabel('Valor de la función')
plt.grid()
plt.show()

# roots Biseccion
roots.append(Biseccion(C, -4.5, -6, tol))
roots.append(Biseccion(C, -3.5, -4.5, tol))

# roots Falsa Posicion
roots.append(Falsa_posicion(C, 0, -3.5, tol))
roots.append(Falsa_posicion(N, -9, -7, tol))

# roots Newton
s = sp.symbols('s')
C1 = s**3 + 12.5*s**2 + 50.5*s + 66
N1 = s**4 + 19*s**3 + 122*s**2 + 296*s + 192

roots.append(Newton(N1,s,-10,tol))
roots.append(Newton(N1,s,-5.7,tol))

# roots Secante
roots.append(Secante(N1, s, 0, -2, tol))

G = ((s + roots[0][0])*(s + roots[1][0])*(s + roots[2][0]))/((s + roots[3][0])*(s + roots[4][0])*(s + roots[5][0])*(s + roots[6][0]))

#print(roots)
print("G(s) =", G)
print("\n--Comparacion de iteraciones--")

lista_intervalos_C=[[-6,-5],[-4.5,-3.75],[-3.5,-2]]
lista_intervalos_N=[[-9,-7.5],[-6.5,-5],[-4.5,-3.5],[-2,0]]

info_C=[]
for intervalo in (lista_intervalos_C):
  a,b=intervalo
  bisec=Biseccion(C,a,b,1e-6)
  falsa=Falsa_posicion(C,a,b,1e-6)
  newton=Newton(C1,s,a,1e-6)
  secante=Secante(C1,s,a,b,1e-6)
  info_C.append([intervalo,bisec[1],falsa[1],newton[1],secante[1]])
d1=pd.DataFrame(data=info_C,columns=["Intervalo","Bisección","Falsa Posición","Newton","Secante"])
print(d1)

info_N=[]
for intervalo in (lista_intervalos_N):
  a,b=intervalo
  bisec=Biseccion(N,a,b,1e-6)
  falsa=Falsa_posicion(N,a,b,1e-6)
  newton=Newton(N1,s,a,1e-6)
  secante=Secante(N1,s,a,b,1e-6)
  info_N.append([intervalo,bisec[1],falsa[1],newton[1],secante[1]])
d2=pd.DataFrame(data=info_N,columns=["Intervalo","Bisección","Falsa Posición","Newton","Secante"])
print(d2)
