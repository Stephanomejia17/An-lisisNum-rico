import numpy as np
import pandas as pd

def Falsa_posicion(f, a, b, tol, particiones = 0):
    if f(a)*f(b) > 0:
        print("La función no cumple el teorema en el intervalo [", a, ", ", b, "] ")
        return 
        
    else:
        i=0
        p = b - f(b) * (a-b) /(f(a)- f(b))
        while (abs(f(p)) > tol):
            p = b - f(b) * (a-b) /(f(a)- f(b))

            i += 1
            if (f(a) * f(p)) > 0:
                a = p
            else:
                b = p
        return p, i
    
"""f= lambda x: x**10 - 1
root = Falsa_posicion(f,0,1.5,1e-8)

print('La solución es: ', root, 'funcion evaluada', f(root[0]), 'cantidad de iteraciones : ', root[1]) # 1e-2 = 10^(-2)"""