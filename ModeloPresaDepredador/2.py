from Euler import euler
import numpy as np
import matplotlib.pyplot as plt

def f (t, u):
    S = u[0]
    I = u[1]
    a = 15
    b = 2385

    f1 = -a * S * I
    f2 = a * S * I - b * I
    return np.array([f1, f2])

tiempo, Modelo = euler(f, 0, 0.01, 0.0001, np.array([254, 7]))

S = np.array(Modelo)[:, 0]
I = np.array(Modelo)[:, 1]
N = 254 + 7
R = N - S - I 

print("Suceptibles: ", I)

plt.figure(figsize=(6,4))
plt.plot(tiempo, S, 'g', label='S')
plt.xlabel('Tiempo')
plt.ylabel('Suceptibles')
plt.show()

plt.figure(figsize=(6,4))
plt.plot(tiempo, I, 'r', label='I')
plt.xlabel('Tiempo')
plt.ylabel('Infecciosa')
plt.show()

plt.figure(figsize=(6,4))
plt.plot(tiempo, R, 'b', label='R')
plt.xlabel('Tiempo')
plt.ylabel('Retirada')
plt.show()