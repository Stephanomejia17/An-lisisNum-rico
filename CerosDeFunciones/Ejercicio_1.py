import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
from Biseccion import Biseccion

g = 32.17
t = 1
x = 1.7

pos = lambda w: -g/(2*w**2) * ((np.exp(w*t) - np.exp(-w*t))/2 - np.sin(w*t)) - x

bisecc = Biseccion(pos, -1, -0.0001, 1e-5)

w = np.linspace(-3, -1e-3, 100)

plt.plot(w, pos(w), 'b')
plt.axhline(0, color='red', linewidth=1, linestyle='dashed')
plt.grid()
plt.show()

print(bisecc)
