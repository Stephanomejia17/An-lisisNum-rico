import numpy as np

def euler (f, a, b, h, y_0):
    weu = [y_0]
    n = int((b-a) /h)
    for i in range(n):
        weu.append(weu[i]+h*f(a+i*h, weu[i]))
    return weu

def f (t, u):
    #u=arreglo de variables u=[w,z] es decir que f(t, [w,z])
    w=u[0]
    z=u[1]
    n=len(u)
    y=np.zeros(n)
    y[0] = z # Ecuacion 1
    y[1] = t*np.exp(t) - t +2* z - w
    return y

f = lambda t, y: t*np.exp(9*t)-2*y
a= 0
b= 1
h=0.25
y0=0


print(f(0.25, [0,0]))

print(euler(f, a,b,h,[0,0]))