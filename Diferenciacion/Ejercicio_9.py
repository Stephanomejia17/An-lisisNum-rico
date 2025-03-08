import numpy as np
import sympy as sp
L = 0.05
R = 2
h = 0.1
t = [1, 1.1, 1.2, 1.3, 1.4]
I = [8.2277, 7.2428, 5.9908, 4.5260, 2.9122]
res = []

for i in range(1, len(t)):
    res.append((I[i]-I[i-1])/h)
    
E = L * res[2] + R * I[2]

t_real = sp.symbols('t_real')
I_real = 10 * sp.exp(-t_real/10) * sp.sin(2*t_real)
dI = sp.diff(I_real, t_real)
I_real = sp.lambdify(t_real, I_real)
dI = sp.lambdify(t_real, dI)
E_real = L * dI(1.2) + R * I_real(1.2)

print("I'(t) aprox: ", res[2], "I'(t) Real: ", dI(1.2))
print("E aprox: ", E, "E Real: ", E_real)