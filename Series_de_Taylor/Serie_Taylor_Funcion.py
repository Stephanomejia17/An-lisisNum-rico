import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import math

x = sp.symbols('x')


def Taylor (f, grado, x0):
    P = f.evalf(subs={x:x0})
    for i in range (1, grado + 1):
        P += (sp.diff(f,x,i)).evalf(subs={x:x0}) * ((x-x0)**i)/math.factorial(i)
        
    return sp.expand(P)

"""P = Taylor(f, 2, x0)
print(P)

delta = 2

u_x = np.linspace(x0-delta, x0+delta, 100)
P=sp.lambdify(x,P)
f=sp.lambdify(x,f)

plt.plot (u_x, f(u_x), 'b', label='$f(x)=Ln(x**2 + 1)$')
plt.plot (u_x, P(u_x), 'r', label='$P(x)=Ln(x**2 + 1)$')

plt.legend()
plt.grid()
plt.xlabel('Eje x')
plt.ylabel('Eje y')

plt.show()"""