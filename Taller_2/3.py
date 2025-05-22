from functions import Euler
from functions import Runge_Kutta_4
import numpy as np
from matplotlib import pyplot as plt

# b.
Ro = 1
gamma = 1.4
a = 10

A = 2.5
h = 1e-7
t_max = 1

R_0 = A*Ro
R_prima_0 = 0

def f_b(t,u):
    
    gamma = 1.4
    a = 10

    w = u[0]
    z = u[1]
    n = len(u)
    f1 = z
    f2 = ((a**2)*((Ro/w)**(3*gamma)-1)-(3/2)*z**2)/w

    return np.array([f1, f2])


tiempo, Modelo = Euler.euler(f_b, 0, t_max, h, [R_0, R_prima_0])

w_euler = np.array(Modelo)[:, 0]
z_euler = np.array(Modelo)[:, 1]

# Procesar resultados
Modelo = np.array(Modelo)
tiempo = np.linspace(0, t_max, len(Modelo))

# Graficar
plt.figure(figsize=(18, 8))
plt.subplot(2, 3, 1)
plt.title("Radio vs Tiempo (Euler)")
plt.plot(tiempo, w_euler, 'b', label='Radio vs Tiempo')
plt.xlabel("Tiempo")
plt.ylabel("Radio")
plt.grid(True)

plt.subplot(2, 3, 2)
plt.title("Radio' vs Tiempo (Euler)")
plt.plot(tiempo, z_euler, 'r', label='Radio` vs Tiempo')
plt.xlabel("Tiempo")
plt.ylabel("Radio'")
plt.grid(True)

# c

def f_c(t,u):
    
    gamma = 1.4
    a = 10

    w = u[0]
    z = u[1]
    n = len(u)
    f1 = z
    f2 = ((a**2)*((Ro/w)**(3*gamma)-1)-(3/2)*z**2)/w

    return np.array([f1, f2])

tiempo, Modelo = Runge_Kutta_4.runge_kutta_4(f_c, 0, t_max, h, [R_0, R_prima_0])
w_runge = np.array(Modelo)[:, 0]
z_runge = np.array(Modelo)[:, 1]

plt.subplot(2, 3, 3)
plt.plot(tiempo, w_runge, 'b', label='Radio vs Tiempo')
plt.title("Radio vs Tiempo (Runge-Kutta 4)")
plt.xlabel("Tiempo")
plt.ylabel("Radio")
plt.grid(True)

plt.subplot(2, 3, 4)
plt.plot(tiempo, z_euler, 'r', label='Radio` vs Tiempo')
plt.title("Radio' vs Tiempo (Runge-Kutta 4)")
plt.xlabel("Tiempo")
plt.ylabel("Radio'")
plt.grid(True)

plt.subplot(2, 3, 5)
plt.plot(w_euler, z_euler, 'g', label='Radio vs Radio` (Euler)')
plt.title("Radio vs Radio` (Euler)")
plt.xlabel("Radio")
plt.ylabel("Radio'")
plt.grid(True)

plt.subplot(2, 3, 6)
plt.plot(w_runge, z_runge, 'm', label='Radio vs Radio` (Runge-Kutta 4)')
plt.title("Radio vs Radio` (Runge-Kutta 4)")
plt.xlabel("Radio")
plt.ylabel("Radio'")
plt.grid(True)

plt.show()


