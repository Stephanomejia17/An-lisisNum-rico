import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from Biseccion import Biseccion
from  Falsa_Posicion import Falsa_posicion
from  Newton import Newton
from Secante import Secante

C = lambda s: s**3 + 12.5*s**2 + 50.5 * s + 66
N = lambda s: s**4 + 19*s**3 + 122*s**2 + 296*s + 192

u_x = np.linspace(-10,2,1000)

roots = []
x0 = -10
x1 = 10
tol = 1e-6

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
print(G)











plt.title('Grafica de funciones')
plt.plot(u_x, N(u_x), 'b')
plt.plot(u_x, C(u_x), 'r')
plt.ylim(-30, 30)

plt.axhline(0, color='black', linestyle='--', linewidth=1.5)
plt.show()