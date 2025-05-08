import numpy as np
import time


def Jacobi_matrices(A, b, tol, x0):
    # Construccion de la matriz Tj del método de Jacobi
    D = np.diag(np.diag(A))
    L = D - np.tril(A)
    U = D - np.triu(A)

    Tj = np.dot(np.linalg.inv(D), L + U) # Elementos de la diagonal son ceros
    Cj = np.dot(np.linalg.inv(D), b)

    v_propios, vect_propios = np.linalg.eig(Tj)
    radio = max(abs(v_propios))

    print(radio)

    if radio < 1: # converge
        tiempo_inicial = time.time()
        error = 1
        while (error > tol):
            x1 = np.dot(Tj, x0) + Cj
            #print(x1)
            error = max(abs(x1 - x0))
            x0 = np.copy(x1)
        
    else:
        print('El sistema iterativo no converge con el metodo de jacobi')
        
    t_final = time.time()
    return x1, t_final - tiempo_inicial
        
"""A = np.array([[3, -1, 0], [-1, 4, -1], [0, -1, 5]], dtype=float)
b = np.array([2, 3, 5], dtype=float)
tol = 1e-6
x0 = np.zeros_like(b)

print(Jacobi_matrices(A, b, tol, x0))"""