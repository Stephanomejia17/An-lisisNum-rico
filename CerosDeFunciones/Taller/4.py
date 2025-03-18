import sys
import os

# Obtiene la ruta absoluta del directorio que contiene 4.py
script_dir = os.path.dirname(os.path.abspath(__file__))

# Obtiene la ruta del directorio padre (CerosDeFunciones)
parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))

# Agrega CerosDeFunciones al path de Python
sys.path.append(parent_dir)

import numpy as np
import sympy as sp
from Biseccion import Biseccion  
from Falsa_Posicion import Falsa_posicion
from Newton import Newton

h = 300
C = 1200
F = 0.8
D = 14
tol = 1e-6

f = lambda A: ((np.pi * ((h/np.cos(A))**2) * F)/(0.5 * np.pi * D**2 * (1 + np.sin(A) - 0.5 * np.cos(A)))) - C


A = sp.symbols('A')
print(f(0), f(np.pi/2))

f2 = ((sp.pi * ((h/sp.cos(A))**2) * F)/(0.5 * sp.pi * D**2 * (1 + sp.sin(A) - 0.5 * sp.cos(A)))) - C


bisecc = Biseccion(f,1,np.pi/2,tol)
falsa = Falsa_posicion(f, 1, np.pi/2, tol)
new = Newton(f2, A, 1, tol)[0] * 180/np.pi

print(bisecc, falsa, new)