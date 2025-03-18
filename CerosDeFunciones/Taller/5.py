import sys
import os

# Obtiene la ruta absoluta del directorio que contiene 4.py
script_dir = os.path.dirname(os.path.abspath(__file__))

# Obtiene la ruta del directorio padre (CerosDeFunciones)
parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

# Agrega CerosDeFunciones al path de Python
sys.path.append(parent_dir)

import sympy as sp
import numpy as np
from Biseccion import Biseccion
from Falsa_Posicion import Falsa_posicion
from Newton import Newton


Lct = 0.088
tol = 1e-6

f = lambda t: - np.sqrt((1/2) * Lct) + np.exp(-(1/2)*t) * np.arccosh(np.exp((1/2)*t))

t = sp.symbols('t')
f1 = sp.sqrt((1/2) * Lct) - sp.exp(-(1/2)*t) * sp.acosh(sp.exp((1/2)*t))


print(Biseccion(f, 1, 100, tol))
print(Falsa_posicion(f, 1, 100, tol))

print(Newton(f1,t,0.1,tol))