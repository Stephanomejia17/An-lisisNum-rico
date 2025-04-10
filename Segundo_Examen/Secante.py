import sympy as sp
import numpy as np
#from Newton import Newton

"""r = 1
V = 0.75
tol = 1e-6"""

def Secante(f, x, x0, x1, tol, iteraciones = 0, resp=[]):
    
    while abs(x1 - x0) > tol:
        
        
        x2 = x1 - (f.evalf(subs={x:x1}) * (x0 - x1)) / (f.evalf(subs={x:x0})-f.evalf(subs={x:x1}))
        resp.append(x2)

        x0 = x1
        x1 = x2
        
        iteraciones += 1
    return x1, iteraciones, resp
    
"""h = sp.symbols('h')
f = (sp.pi * h**2 * (3*r - h))/3 - V

print(Secante(f, h, 1, 2, tol), Newton(f,h,1,tol))"""