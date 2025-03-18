from Biseccion import Biseccion
from Falsa_Posicion import Falsa_posicion
from Newton import Newton
import numpy as np
import sympy as sp
import pandas as pd

V = 0.75
r = 1
tol = 1e-6
x = sp.symbols('x')


f = lambda h: ((np.pi * h**2 * (3*r - h))/3) - V
f_x = ((sp.pi * x ** 2 * (3*r-x))/3) - V

bisecc = Biseccion(f,0, 2, tol)
falsa = Falsa_posicion(f, 0, 2, tol)
new = Newton(f_x, x, 1, tol)

data = []

for i in range(0, len(bisecc[2])):
    data.append(bisecc[2][i])
    
print(data)