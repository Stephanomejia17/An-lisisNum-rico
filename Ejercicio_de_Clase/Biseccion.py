import numpy as np
import pandas as pd

def Biseccion(f, a, b, tol, particiones = 0):
    if f(a)*f(b) > 0:
        print("La función no cumple el teorema en el intervalo [", a, ", ", b, "] ")
        
    else:
        print("Buscando")
        while (abs(b-a) > tol):
            particiones += 1
            p = (a+b)/2
            if f(a) * f(p) > 0:
                a = p
            else:
                b = p
        return p, particiones
    
"""f= lambda x: (3**(-x))-x
root = Biseccion(f,0,1,1e-8)

print('La solución es: ', root, 'funcion evaluada', f(root[0]), 'cantidad de iteraciones : ', root[1]) # 1e-2 = 10^(-2)"""