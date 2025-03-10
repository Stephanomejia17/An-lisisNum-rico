import numpy as np
import sympy as sp

h = 0.0001
k = np.log(2)/3
x0 = 1000
res = [x0]

P_t_Real = lambda t: 1000 * np.exp(k*t)

i = 0
while i <= 3:
    res.append(1000*h*res[-1] + res[-1])
    
    i += h
    
print(res[2], P_t_Real(3))

# no daz