import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math

x = sp.symbols('x')


def Taylor (f, grado, x0):
    P = f.evalf(subs={x:x0})
    for i in range (1, grado + 1):
        P += (sp.diff(f,x,i)).evalf(subs={x:x0}) * ((x-x0)**i)/math.factorial(i)
        
    return sp.expand(P)

