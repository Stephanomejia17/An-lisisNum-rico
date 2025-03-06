import sympy as sp
from Serie_Taylor_Funcion import Taylor

x = sp.symbols('x')
f = 2**(-x)
x0 = 0

for i in range(1, 3):
    
    res = Taylor(f, i, x0)
    print("Polinomio de grado ", i, ": ", res)

