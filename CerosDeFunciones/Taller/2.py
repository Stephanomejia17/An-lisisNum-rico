import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def Biseccion(f,a,b,tol):
  if f(a)*f(b)>0:
    print('La funcion cumple el teorema')
    return
  else:
    print('seguir buscando')
    num_iteracion=0
    while(abs(b-a)> tol):
      p= (a+b)/2
      num_iteracion+=1
      if f(a)*f(p)>0:
        a=p
      else:
        b=p
    return p,num_iteracion

c=0.1221
p=34.12

f= lambda w: np.tan(w/3-1) -((2*c*(w/p))/1-(w/p)**2)

#Grafica
w= np.linspace(0,30,500)
plt.axhline(0,color='black')
plt.ylim(-50, 50)
plt.plot(w,f(w))
plt.title('Grafica de la funcion f(w)')
plt.xlabel('w')
plt.ylabel('f(w)')
plt.grid()
plt.show()

Biseccion1=Biseccion(f,0,10,1e-6)
print(Biseccion1)
Biseccion2=Biseccion(f,10,15,1e-6)
print(Biseccion2)
Biseccion3=Biseccion(f,25,27,1e-6)
print(Biseccion3)