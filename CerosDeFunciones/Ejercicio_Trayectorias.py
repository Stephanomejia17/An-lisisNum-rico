import numpy as np
from Biseccion import Biseccion
x = 35
g = 9.8
vo = 20
yo = 2
y = 1

f_tray = lambda o: x*np.tan(o) - (g*x**2)/(2*(vo**2)*(np.cos(o))**2) + yo- y # o es el angulo

root = Biseccion(f_tray, 0, np.pi/4, 1e-6)

print("theta_inicial:", np.degrees(root[0]), "°", "iteracion_theta:", root[1])