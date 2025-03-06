from Biseccion import Biseccion
from Falsa_Posicion import Falsa_posicion
from Newton import Newton
import numpy as np
import sympy as sp

L = 10
r = 1
V = 10
tol = 1e-3

f1 = lambda h: (L * ((1/2)*np.pi*r**2 - r**2 * np.arcsin(h/r) - h * (r**2 - h**2)**(1/2))) - V

h = sp.symbols('h')
f2 = (L * ((1/2)*np.pi*r**2 - r**2 * sp.asin(h/r) - h * (r**2 - h**2)**(1/2))) - V

bisecc = Biseccion(f1, 0, 1, tol)
falsa_posicion = Falsa_posicion(f1, 0, 1, tol)
newton = Newton(f2, h, 0, tol)


print("Biseccion: ", 1-bisecc[0], "iteraciones: ", bisecc[1])
print("Falsa Posicion: ", 1-falsa_posicion[0], "iteraciones: ", falsa_posicion[1])
print("Newton: ", 1-newton[0], "iteraciones: ", newton[1])