from Serie_Taylor_Funcion import Taylor
from Cota import Cota_de_Error
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')
f = (1+x)**2 * sp.log(1+x)
x0 = 0


P2 = Taylor(f, 2, x0)


print("1. Polinomio grado 2", P2)

print("2. f evaluado en 0.5: ", f.evalf(subs={x:0.5}))
print("2. P2 evaluado en 0.5: ", P2.evalf(subs={x:0.5}))

print("2. Cota aproximada de error: ", Cota_de_Error(f,x,x0,0.5,2)[0])
print("2. Cota real de error: ", abs(f.evalf(subs={x:0.5})-P2.evalf(subs={x:0.5})))

integral = sp.integrate(P2,(x, -0.5, 0.5))
print(P2)
P2 = sp.lambdify(x, P2)

f = sp.lambdify(x, f)


print(integral)

