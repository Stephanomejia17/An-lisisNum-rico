import numpy as np
from functions import Euler
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

tiempo, Modelo = Euler.euler(f, 0, 10, 0.01, np.array([0, 0]))

a = np.array(Modelo)[:, 0]
b = np.array(Modelo)[:, 1]

Modelo = np.array(Modelo)
tiempo = np.linspace(0, 10, len(Modelo))

print(max(a))

plt.plot(tiempo, a, label='a')
# plt.plot(tiempo, b, label='b')
# plt.plot(a, b, label='a vs b')
plt.title('Euler')
plt.xlabel('Tiempo')
plt.ylabel('Theta')
plt.show()
