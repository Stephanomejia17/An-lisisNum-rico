import numpy as np

def Gauss(a, b):
    n = len(b)
    respuesta = np.zeros(n)
            
    for i in range(n-1):
        for j in range(i+1, n):
            factor_lambda = a[j, i] / a[i, i]
            a[j] = a[j] - factor_lambda * a[i]
            b[j] = b[j] - factor_lambda * b[i]
        
            
    for i in range(n-1, -1, -1):
        respuesta[i] = (b[i] - np.dot(a[i, i+1:n], respuesta[i+1:n]))/a[i,i]
    return a, b, respuesta

def Gauss_con_pivoteo(a, b):
    n = len(b)
    respuesta = np.zeros(n)
    i = 0
            
    while True:
        if i == n-1:
            break
        if a[i,i] != 0:
            for j in range(i+1, n):
                factor_lambda = a[j, i] / a[i, i]
                a[j] = a[j] - factor_lambda * a[i]
                b[j] = b[j] - factor_lambda * b[i]
            i += 1
        else:
            aux = a[i].copy()
            aux_b = b[i].copy()
            a[i] = a[i+1]
            b[i] = b[i+1]
            a[i+1] = aux
            b[i+1] = aux_b
        
    for i in range(n-1, -1, -1):
        respuesta[i] = (b[i] - np.dot(a[i, i+1:n], respuesta[i+1:n]))/a[i,i]
    return a, b, respuesta
            
    
        
a = np.array([[0, 2, 1], [6, 0, -2], [1, -1 ,-2]])
b = np.array([2,1,3])

a = a.astype(float)
b = b.astype(float)


a,b, res = Gauss_con_pivoteo(a,b)

print(a)
print(b)
print(res)

