import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

x = sp.symbols('x')

def serie_taylor(f, x0, n):
    # f: funcion
    # x0: punto al rededor donde se construye la serie
    # n: grado del polinomio
    P=0
    for i in range(n+1):
        df=sp.diff(f,x,i)
        dfe = df.evalf(subs={x:x0})
        P+=dfe*(x-x0)**i/factorial(i)
    
    return sp.expand(P)

f = 2**x

P1 = serie_taylor(f, 0, 1)
print(P1)
P1 = sp.lambdify(x, P1)
print(P1(0.5))

