import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from math import factorial
import pandas as pd

k = -0.4056
h=0.0001
Ta=27


x=[37]
t=[0]

while True:
    if x[-1] <= 30:
        break
    else:
        x.append(h*k*(x[-1]-Ta)+x[-1])
        t.append(t[-1]+h)
     
print("hora aproximada de fallecimiento: ", 12-t[-1], " horas")

plt.xlabel('Tiempo (horas)')
plt.ylabel('Temperatura (C)')

plt.plot(t, x, color='b')
plt.show()
