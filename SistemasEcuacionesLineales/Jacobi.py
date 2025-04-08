import numpy as np
import time
"""
----------------------------------------------------------------------------------------
A: Matriz cuadrada NxN
b: vector 
x0: vector inicial ---> si no me dan este dato se asume que el vector es el vector nulo
Nmax: Numero máximo de iteraciones de la sucesión
tol: Exactitud con la cual encontraremos la solución de sistema de ecuaciones lineales SEL 
    --> Si no me proporcionan este dato, se asume como 1e-6
NOTA: TANTO LA MATRIZ COMO EL VECTOR b Y X0 TIENEN QUE SER DE TIPO FLOTANTE
----------------------------------------------------------------------------------------
"""


def Jacobi_sumas(A, b, x0, Nmax, tol=1e-6):
    n = len(b)
    x_sol = np.zeros(n)
    error = 10
    cont = 0
    
    t_inicial = time.time()
    while error > tol and Nmax>cont:
        
        for i in range(n):
            suma = 0
            for j in range(n):
                if (i != j):
                    suma += np.dot(A[i,j], x0[j])
                    
            x_sol[i] = (b[i] - suma)/A[i, i]
            
            
        error = max(abs(x_sol - x0))
        x0 = x_sol.copy()        
        cont += 1
    t_final = time.time()
    
    print(t_inicial, t_final)
        
    
    
    return x_sol, t_final - t_inicial

A = np.array([[3, -1, 0], [-1, 4, -1], [0, -1, 5]], dtype=float)
b = np.array([2, 3, 5], dtype=float)

x0 = np.zeros(len(b))


x_sol, tiempo = Jacobi_sumas(A, b, x0, 50, 1e-2)



print(x_sol, tiempo)
