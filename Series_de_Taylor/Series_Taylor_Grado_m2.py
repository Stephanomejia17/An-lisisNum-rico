import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from math import factorial
import pandas as pd

from Serie_Taylor_Funcion import Taylor

x = sp.symbols('x')
x0 = 0
grados = [1,2]
valores_a_evaluar = [1, 5]

def serie_taylor(f, x0, n):
    # f: funcion
    # x0: punto al rededor donde se construye la serie
    # n: grado del polinomio
    P=f.evalf(subs={x:x0})
    for i in range(n+1):
        df=sp.diff(f,x,i)
        dfe = df.evalf(subs={x:x0})
        P+=(dfe*(x-x0)**i)/factorial(i)
    
    return sp.expand(P)

f = sp.log(x**2 + 1)
info = []


for i in grados:
    print("Polinomio de grado: ", i, "es ",serie_taylor(f, x0, i))
    for j in valores_a_evaluar:
        P_aprox = sp.lambdify(x, serie_taylor(f,x0,i))(j)
        F_real = f.evalf(subs={x:j})
        E_abs = np.abs(P_aprox-F_real)
        E_rel = np.abs(E_abs/F_real)

        info.append([i, j, P_aprox, F_real, E_abs, E_rel, str(E_abs*100) + '%', str(E_rel*100) + '%'])
        
d = pd.DataFrame(data=info, columns=['Grado de derivada', 'X', 'P(X)', 'F(X)', 'Ea=|P(X)-f(X)|', 'Er', 'Eap (%)', 'Erp (%)'])
print("\n", d)




