from Jacobi_2 import Jacobi_matrices
from gauss_seidel import gauss_seidel
import matplotlib.pyplot as plt
import numpy as np

Px = np.array([1,2,5,10,20,30,40])
Ty = np.array([56.5, 78.6, 113, 144.5,181.0,205.0,214.5])

def Matrix (Px):
    n = len(Px)
    B = np.zeros([n, n])
    for i in range(n):
        B[i, 0] = 1
        for j in range(1, n):
            B[i,j] = B[i,j-1] * Px[i]
        
    return B
    
    

Px = np.array([1,2,5,10,20,30,40])
Ty = np.array([56.5, 78.6, 113, 144.5,181.0,205.0,214.5])        
tol = 1e-6
x0 = np.zeros_like(Ty)
coef = gauss_seidel(Matrix(Px), Ty, tol, x0)
Pol = lambda x: coef[0]+coef[1]*x + coef[2]*x**2 + coef[3]*x**3 + coef[4]*x**4 + coef[5]*x**5 + coef[6]*x**6 

    
u_x = np.linspace(min(Px), max(Px), 100)
plt.plot(Px, Ty, 'o', label='Datos Observados')
plt.plot(u_x, Pol(u_x), label='Polinomio grado 1')
plt.legend()
plt.show()







"""A = np.array([[1,1,1], [1,5, 25], [1, 20, 400]], dtype=float)
b = np.array([56.5, 113, 181], dtype=float)
tol = 1e-6
x0 = np.zeros_like(b)
coef = gauss_seidel(A,b,tol,x0)
Pol = lambda x: coef[0]+coef[1]*x + coef[2]*x**2
u_x = np.linspace(min(Px), max(Px), 100)
plt.plot(Px, Ty, 'o', label='Datos Observados')
plt.plot(u_x, Pol(u_x), label='Polinomio grado 1')
plt.legend()
plt.show()

print(Jacobi_matrices(A, b, tol, x0))"""