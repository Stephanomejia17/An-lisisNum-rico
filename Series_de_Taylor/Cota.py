import sympy as sp
import numpy as np
import math

def Cota_de_Error(f, x, x0, x_point, n):
    df = sp.diff(f, x, n+1)
    df = sp.lambdify(x, df)
    u_x = np.linspace(x0, x_point, 1000)

    Maximo = np.max(np.abs(df(u_x)))
    
    R = Maximo * ((x_point - x0)**(n+1)) / (math.factorial(n+1))
    
    return R, Maximo
    
    
