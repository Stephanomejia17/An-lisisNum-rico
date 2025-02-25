import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
# Declarar x como variable simbolica


x = sp.symbols('x')
f=2**x
df = sp.diff(f, x)
# Segunda derivada
df2 = sp.diff(f,x,2)

x0 = 0


# P=f(x0) + f'(x0) * (x-x0)
P2=f.evalf(subs={x:x0}) + df.evalf(subs={x:x0}) * (x-x0) + df2.evalf(subs={x:x0})*(x-x0)**2/2

# Gráfica del polinomio versus la función

delta = 2

u_x = np.linspace(x0-delta, x0+delta, 100)
P2=sp.lambdify(x,P2)
f=sp.lambdify(x,f)

plt.plot (u_x, f(u_x), 'b', label='$f(x)=2^x$')
plt.plot (u_x, P2(u_x), 'r', label='$P(x)=2^x$')

plt.legend()
plt.xlabel('Eje x')
plt.ylabel('Eje y')

plt.show()