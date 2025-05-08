import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def Lagrange(x_list: list[float], y_list: list[float]): 
    x = sp.symbols('x')
    P_x = 0
    
    if (len(x_list) != len(y_list)):
        print("Error: No se puede usar Lagrange sin la relación uno a uno")
        return
    
    for i in range(len(y_list)):
        L_x = 1
        for j in range(len(x_list)):
            if j == i:
                continue
            L_x *= (x - x_list[j])/(x_list[i] - x_list[j])
        P_x += L_x * y_list[i]
    return sp.lambdify(x, P_x), sp.expand(P_x)