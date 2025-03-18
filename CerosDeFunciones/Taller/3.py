import numpy as np

A = np.exp(1) * 1/3

f = lambda t: A*t*np.exp(-t/3)

print(f(3))