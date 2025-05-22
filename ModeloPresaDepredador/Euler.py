import numpy as np

def euler (f, a, b, h, yo):
    weu = [yo]
    n = int((b-a) /h)
    for i in range(n):
        weu.append(weu[i]+h*f(a+i*h, weu[i]))
    return  np.linspace(a, b, n+1), weu

def f (t, u):
    #u=arreglo de variables u=[w,z] es decir que f(t, [w,z])
    w=u[0]
    z=u[1]
    n=len(u)
    y=np.zeros(n)
    y[0] = z # Ecuacion 1
    y[1] = t*np.exp(t) - t +2* z - w
    return y

"""f = lambda t, y: t*np.exp(3*t)-2*y
a= 0
b= 1
h=0.25
y0=0"""


# print(euler(f, 0, 1, 0.25, [0,0]))