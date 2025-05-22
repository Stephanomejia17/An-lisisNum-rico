from Euler import euler
from Runge_Kutta_4 import runge_kutta_4
import numpy as np
from matplotlib import pyplot as plt

c_1 = [0.5, 1.5, 2.2, 3]
c = 0.5
DENISEVSCRAIG = "Denise vs Craig"
RUNGEKUTTA4 = "Runge-Kutta 4"

def f(t, u):
    x1 = u[0]
    y1 = u[1]
    
    x_prima = y1 + np.sin(c*t)
    y_prima = -4*x1

    return np.array([x_prima, y_prima])



tiempo, Modelo = euler(f, 0, 24, 0.01, np.array([0, 0]))
x = np.array(Modelo)[:, 0]
y = np.array(Modelo)[:, 1]
plt.title('Euler')
plt.plot(tiempo, x, label='x1')
plt.plot(tiempo, y, label='x2')
plt.show()

tiempo, Modelo = euler(f, 0, 24, 0.01, np.array([0, 0]))

plt.plot(x, y, label=DENISEVSCRAIG)
plt.xlabel('Denise')
plt.ylabel('Craig')
plt.title(DENISEVSCRAIG)
plt.show()

c = 1.5
tiempo, Modelo = euler(f, 0, 24, 0.01, np.array([0, 0]))
x = np.array(Modelo)[:, 0]
y = np.array(Modelo)[:, 1]
plt.title('Euler')
plt.plot(tiempo, x, label='x1')
plt.plot(tiempo, y, label='x2')
plt.show()

tiempo, Modelo = euler(f, 0, 24, 0.01, np.array([0, 0]))

plt.plot(x, y, label=DENISEVSCRAIG)
plt.xlabel('Denise')
plt.ylabel('Craig')
plt.title(DENISEVSCRAIG)
plt.show()

c = 2.2

tiempo, Modelo = euler(f, 0, 24, 0.01, np.array([0, 0]))
x = np.array(Modelo)[:, 0]
y = np.array(Modelo)[:, 1]
plt.title('Euler')
plt.plot(tiempo, x, label='x1')
plt.plot(tiempo, y, label='x2')
plt.show()

tiempo, Modelo = euler(f, 0, 24, 0.01, np.array([0, 0]))

plt.plot(x, y, label=DENISEVSCRAIG)
plt.xlabel('Denise')
plt.ylabel('Craig')
plt.title(DENISEVSCRAIG)
plt.show()

c = 3

tiempo, Modelo = euler(f, 0, 24, 0.01, np.array([0, 0]))
x = np.array(Modelo)[:, 0]
y = np.array(Modelo)[:, 1]
plt.title('Euler')
plt.plot(tiempo, x, label='x1')
plt.plot(tiempo, y, label='x2')
plt.show()

tiempo, Modelo = euler(f, 0, 24, 0.01, np.array([0, 0]))

plt.plot(x, y, label=DENISEVSCRAIG)
plt.xlabel('Denise')
plt.ylabel('Craig')
plt.title(DENISEVSCRAIG)
plt.show()

# Runge-Kutta
c = 0.5
tiempo, Modelo = runge_kutta_4(f, 0, 24, 0.01, np.array([0, 0]))
x = np.array(Modelo)[:, 0]
y = np.array(Modelo)[:, 1]

plt.title(RUNGEKUTTA4)
plt.plot(tiempo, x, label='x1')
plt.plot(tiempo, y, label='x2')
plt.show()

tiempo, Modelo = runge_kutta_4(f, 0, 24, 0.01, np.array([0, 0]))
plt.plot(x, y, label=DENISEVSCRAIG)
plt.xlabel('Denise')
plt.ylabel('Craig')
plt.title(DENISEVSCRAIG)
plt.show()

c= 1.5
tiempo, Modelo = runge_kutta_4(f, 0, 24, 0.01, np.array([0, 0]))
x = np.array(Modelo)[:, 0]
y = np.array(Modelo)[:, 1]
plt.title(RUNGEKUTTA4)
plt.plot(tiempo, x, label='x1')
plt.plot(tiempo, y, label='x2')
plt.show()

tiempo, Modelo = runge_kutta_4(f, 0, 24, 0.01, np.array([0, 0]))
plt.plot(x, y, label=DENISEVSCRAIG)
plt.xlabel('Denise')
plt.ylabel('Craig')
plt.title(DENISEVSCRAIG)
plt.show()

c = 2.2
tiempo, Modelo = runge_kutta_4(f, 0, 24, 0.01, np.array([0, 0]))
x = np.array(Modelo)[:, 0]
y = np.array(Modelo)[:, 1]
plt.title(RUNGEKUTTA4)
plt.plot(tiempo, x, label='x1')
plt.plot(tiempo, y, label='x2')
plt.show()

tiempo, Modelo = runge_kutta_4(f, 0, 24, 0.01, np.array([0, 0]))
plt.plot(x, y, label=DENISEVSCRAIG)
plt.xlabel('Denise')
plt.ylabel('Craig')
plt.title(DENISEVSCRAIG)
plt.show()

c = 3
tiempo, Modelo = runge_kutta_4(f, 0, 24, 0.01, np.array([0, 0]))
x = np.array(Modelo)[:, 0]
y = np.array(Modelo)[:, 1]
plt.title(RUNGEKUTTA4)
plt.plot(tiempo, x, label='x1')
plt.plot(tiempo, y, label='x2')
plt.show()

tiempo, Modelo = runge_kutta_4(f, 0, 24, 0.01, np.array([0, 0]))
plt.plot(x, y, label=DENISEVSCRAIG)
plt.xlabel('Denise')
plt.ylabel('Craig')
plt.title(DENISEVSCRAIG)
plt.show()