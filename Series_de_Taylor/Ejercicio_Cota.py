import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import pandas as pd
# Declarar x como variable simbolica


x = sp.symbols('x')
f=2**x
df = sp.diff(f, x, 4)
df=sp.lambdify(x,df)
x0 = 0
x_point = 0.5
u_x = np.linspace(x0, x_point, 1000)
Maximo =np.max(np.abs(df(u_x)))
print(Maximo)
R_x=Maximo*(x_point-x0)**4/sp.factorial(4)
print(R_x)

info = []

def cota(f, x0, list_derivadas = [], data=[]):
    for i in list_derivadas:
        df = sp.diff(f,x,i)
        df=sp.lambdify(x,df)
        Maximo =np.max(np.abs(df(u_x)))
        R_x=Maximo*(x_point-x0)**4/sp.factorial(4)
        data.append([Maximo, R_x])
    return data



info = cota(f,0)

d = pd.DataFrame(data=info, columns=['Maximo', 'R_x'])

print(info)
print (d)



"""print(solve( Eq( df, 0 ) ))
u_x = np.linspace(x0, x_point, 1000)
Maximo = np.max(np.abs(df(u_x)))
print(Maximo)"""

