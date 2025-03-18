import numpy as np
import pandas as pd

def Biseccion(f, a, b, tol, particiones = 0, rpta = [], sign = ''):
    if f(a)*f(b) > 0:
        print("La función no cumple el teorema en el intervalo [", a, ", ", b, "] ")
        
    else:
        print("Buscando")
        while (abs(b-a) > tol):
            rpta.append([])
            particiones += 1
            p = (a+b)/2
            
            if f(a) * f(p) > 0:
                sign = 'positivo'
                a = p
            else:
                sign = 'negativo'
                b = p
            
                          
            
            rpta[-1].append(a)
            rpta[-1].append(b)
            rpta[-1].append(sign)
        return p, particiones, rpta
    
"""f= lambda x: (3**(-x))-x
root = Biseccion(f,0,1,1e-8)

print('La solución es: ', root, 'funcion evaluada', f(root[0]), 'cantidad de iteraciones : ', root[1]) # 1e-2 = 10^(-2)"""