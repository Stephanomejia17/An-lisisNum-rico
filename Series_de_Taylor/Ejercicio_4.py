import sympy as sp
from Serie_Taylor_Funcion import Taylor
from Cota import Cota_de_Error
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
f = sp.exp(2*x)* sp.cos(2*x)
x0 = 0
grados = [1, 2, 4, 6]
polinomios = []
polinomios_lambdify = []

res = Taylor(f, 3, x0)
print("Polinomio de grado ", 3, ": ", res)

for i, valor in enumerate(grados):
    polinomios.append(Taylor(f, valor, x0))
    polinomios_lambdify.append(sp.lambdify(x, polinomios[-1]))
    
print(polinomios_lambdify)

cota_error = Cota_de_Error(f, x, x0, 0.5, 3)

res = sp.lambdify(x, res)
f = sp.lambdify(x,f)
print("(1): ", res(1), "(4.5): ", res(4.5))
print("(1): ", f(1), "(4.5): ", f(4.5))
print("Cota de error: ", cota_error[0])
print("Error relativo: ", abs((f(1)-res(1))/f(1)))
print("Error absoluto: ", abs((f(1)-res(1))))

u_x = np.linspace(-10, 10, 1000)
plt.plot(u_x, polinomios_lambdify[0](u_x), 'r')
plt.plot(u_x, polinomios_lambdify[1](u_x), 'b')
plt.plot(u_x, polinomios_lambdify[2](u_x), 'g')
plt.plot(u_x, polinomios_lambdify[3](u_x), 'c')

plt.show()

