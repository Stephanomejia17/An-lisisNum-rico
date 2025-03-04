import sympy as sp
import numpy as np
from Serie_Taylor_Funcion import Taylor
from Cota import cota
import matplotlib.pyplot as plt
import pandas as pd
import math 

x = sp.symbols('x')
x0 = 0

f = sp.exp(2*x)*sp.sin(x)

P = Taylor(f, 3, x0)

df4 = sp.diff(f, x, 4)
print("Cuarta derivada: ", df4)
df4 = sp.lambdify(x, df4)
u_x = np.linspace(x0, 1, 10000)

Maximo =np.max(np.abs(df4(u_x)))

P=sp.lambdify(x,P)
f=sp.lambdify(x,f)

P1 = P(1)
P2 = P(4.5)
f1 = f(1)
f2 = f(4.5)

E4 = ((x - x0)**4)

R3 = Maximo * E4 / math.factorial(4)

info = [[1, P1, f1, sp.Abs(f1-P1), sp.Abs(f1-P1)/sp.Abs(f1)], [4.5, P2, f2, sp.Abs(f2-P2) , sp.Abs(f2-P2)/sp.Abs(f2)]]

d = pd.DataFrame(data=info, columns=['Evaluacion', 'P(x)', 'f(x)', 'Error Absoluto', 'Error Relativo'])

R3 = sp.lambdify(x, R3)

print("Máximo: ", Maximo)
print("Cota de Truncamiento R(3): ", R3(1))
print(d)
