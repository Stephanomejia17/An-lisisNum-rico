import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from math import factorial
import pandas as pd

# Ejemplo de contagios
# x: cantidad contagiados
# 1000-x: cantidad de los no infectados
# t0 = Tiempo inicial (t=0)
# tf = Supongan dependiendo del problema y la pregunta
# h: dependiendo de la unidad de tiempo del problema
# h=1 <=====> una unidad de tiempo (años, días, meses, semanas, horas, minutos, segundos, etc)
# h = 0.5 <====> la mitad de una unidad
# h=0.01 <==> 24 minutos

x=[1]
h=0.01
t0 = 0
k=0.0009906
t_final = 0
t=[0]

while t_final <= 6:
    x.append(h*k*x[-1]*(1000-x[-1]) + x[-1])
    t.append(t[-1]+h)
    t_final += h



plt.plot(t,x, color='b')    
plt.grid()
plt.show()