import numpy as np
from functions import Euler
from functions import Runge_Kutta_4 
from matplotlib import pyplot as plt

g = 9.80665
L = 1
Y = 0.25
w = 2.5
t = 0
y_0 = Y*np.sin(w*t)

def f(t, u):
    a = u[0]
    b = u[1]
    n = len(u)
    f1 = b
    f2 = -g/L * np.sin(a) + (w**2)/L * Y * np.cos(a) * np.sin(w*t)
    return np.array([f1, f2])

tiempo_euler, Modelo_euler = Euler.euler(f, 0, 10, 0.00001, np.array([np.pi/6, 0]))
timpo_runge, Modelo_runge = Runge_Kutta_4.runge_kutta_4(f, 0, 10, 0.01, [np.pi/6, 0])

a = np.array(Modelo_euler)[:, 0]
b = np.array(Modelo_euler)[:, 1]

c = np.array(Modelo_runge)[:, 0]
d = np.array(Modelo_runge)[:, 0]

Modelo_euler = np.array(Modelo_euler)
tiempo_euler = np.linspace(0, 10, len(Modelo_euler))

Modelo_runge = np.array(Modelo_runge)
tiempo_runge = np.linspace(0, 10, len(Modelo_runge))

print("Valor más grande de theta con Euler: ", max(a), (max(a)*(180/np.pi)))
print("Valor más grande de theta con Runge-Kutta: ", max(c), (max(c)*(180/np.pi)))


plt.plot(tiempo_euler, a)
plt.title('Euler')
plt.title('Euler')
plt.xlabel('Tiempo')
plt.ylabel('Theta')
plt.grid(True)
plt.show()

plt.plot(tiempo_runge, c)
plt.title('Runge-kutta')
plt.xlabel('Tiempo')
plt.ylabel('Theta')
plt.grid()

plt.show()
