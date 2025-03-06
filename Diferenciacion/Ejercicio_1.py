from Diferenciacion_progresiva import progresiva
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1.2,1.29,1.3,1.31,1.4])
f = np.array([11.59006, 13.78176, 14.04276, 14.30741, 16.86187])

x0 = 1.3

h = 0.1

print("1. ", (f[4] - f[2])/h)

h = 0.01

print("2. ", (f[3] - f[2])/h)

h = 0.1

print("3. ", (f[4] - f[0])/(2*h))

h = 0.01

print("4. ", (f[3] - f[1])/(2*h))

print("\nValor real: ", 26.28170519)