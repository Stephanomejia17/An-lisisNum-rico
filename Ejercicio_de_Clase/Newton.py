"""
   Método Abierto, no se requiere conocer el intervalo donde esta el root
   
   Su dificultad radica en el calculo de la derivada y si se presentan raíces repetidas. 
   Se deduce del teorema de Taylor al tomas el polinomio de grado 1 
   
   se requiere un punto inicial 
    y la derivada 
    
    x0 -> punto inicial de la raiz
    
    Newton/alpha = x0 - (f(x0)/f'(x0)) con f'(x0) != 0
    ó
    x_(n+1) = x_n - (f(x_n)/f'(x_n)) para n >= 1
    
    
    Calcular la aproximación de x^{2}-6=0
    Con exactitud de 10^{-4} -> (Al menos 5 cifras)
    
        f(x) = x^{2} - 6
        f'(x) = 2x 
        x0 = 1 
        
    iteracion 1 :
        x1 = x0 - (f(x0)/f'(0))
            = 1 - f(1)/f'(1) = 7/2 aprox 3.5
            
        Error: |Xactual - Xanterior| = |X1 -X0| = |3.5 - 1| = 2.5
     
    iteracion 2:
        x2 = x1 - f(x1)/f'(x1) = 3.5 - f(3.5)/f'(3.5) = 3.5 - ((3.5^{2}-6)/2*(3.5)) = 2.60714
        Error: |x2 - x1| = |3.5 - 2.60714| = 0.89286
        
    
    iteracion 3:
        x3 = x2 - f(x2)/f'(x2) = 2.60714 - f(2.60714)/f'(2.60714) = 2.60714 - ((2.60714^{2}-6)/2*(2.60714)) = 2.45425
        Error: |x2 - x1| = |2.45425 - 2.60714| = 
        
    iteracion 4:
        x4 = x3 - f(x3)/f'(x3) = 2.45425 - f(2.45425)/f'(2.45425) = 2.45425 - ((2.45425^{2}-6)/2*(2.45425)) = 2.44949
        Error: |x3 - x1| = |2.44949 - 2.45425| = 

"""
import sympy as sp
import numpy as np

def Newton(f, x, x0, tol, iteraciones = 0):
    df = sp.diff(f, x)
    
    x1 = (x0 - f.evalf(subs={x:x0})/df.evalf(subs={x:x0}))
    
    while abs(x1 - x0) > tol:
        x0 = x1
        x1 = (x0 - f.evalf(subs={x:x0})/df.evalf(subs={x:x0}))
        iteraciones += 1

    return x1, iteraciones
    
"""x = sp.symbols('x')
f = x**2 - 6
x0 = 1

rpt = Newton(f, x, x0, 1e-5)
print(rpt)"""