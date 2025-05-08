"""
Lagrange:

P(x) : L_0(x) * y_0 + L_1(x) * y_1 + L_2(x) * y_2

y_n son valores numericos
L_n(x) son Polinomios de Lagrange de grado n 
"""
import Lagrange   
import numpy as np
import matplotlib.pyplot as plt  
            
x = [0, 0.6, 0.9]
y = [1.000, 1.264911, 1.378404]

res = Lagrange(x, y)

print("Evaluando: ", res[0](0.6), "\nPolinomio: ", res[1])

u_x = np.linspace(min(x), max(x), 100)
plt.plot(x, y, 'gp', label='Datos Observados')
plt.plot(u_x, res[0](u_x), 'r', label='Polinomio')
plt.legend()
plt.show()





    