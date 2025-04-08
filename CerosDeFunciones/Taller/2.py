import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from Biseccion import Biseccion

c=0.1221
p=34.12

f= lambda w: np.tan(w/3-1) -((2*c*(w/p))/1-(w/p)**2)

#Grafica
w= np.linspace(0,2*np.pi,10000)
plt.axhline(0,color='black')
plt.plot(w,f(w))
plt.title('Grafica de la funcion f(w)')
plt.xlabel('w')
plt.ylabel('f(w)')
plt.show()

Bisec=Biseccion(f,0,np.pi,1e-6)
print("w =", Bisec[0]*180/np.pi, "grados")