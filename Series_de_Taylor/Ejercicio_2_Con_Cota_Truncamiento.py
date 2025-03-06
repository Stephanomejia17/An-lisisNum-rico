import sympy as sp
import numpy as np
import pandas as pd
from Serie_Taylor_Funcion import Taylor
from Cota import Cota_de_Error

x = sp.symbols('x')
f = sp.exp(2*x) * sp.sin(x)
x0 = 0

grados = [1, 2, 3, 4, 6]
puntos = [1, 4.5]
polinomios = []
polinomios_lambdify = []
info = []

for i in grados:
    polinomios.append(Taylor(f, i, x0))
    polinomios_lambdify.append(sp.lambdify(x, polinomios[-1]))
    

for i, polinomio in enumerate(polinomios_lambdify):
    info.append([])
    for j in puntos:
        info[i].append(polinomio(j))
    
cota_error, maximo = Cota_de_Error(f,x,x0,1,3)


# impresiones
for i, valor in enumerate(grados):
    print("Polinomio grado ", valor, ": ", polinomios[i])

f = sp.lambdify(x, f)
print("Cota de Error: ", cota_error, " Maximo: ", maximo)
print(polinomios_lambdify[2](4.5))
print(f(4.5))