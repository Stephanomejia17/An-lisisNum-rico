from MinimosCuadrados import MinimosCuadrados
import numpy as np
import matplotlib.pyplot as plt

x = np.array([100, 200, 300, 400, 500, 600, 700, 800])
y = np.array([205, 430, 677, 945, 1233, 1542, 1872, 2224])

a = MinimosCuadrados(y, x)

p = lambda x: a[0] + a[1] * x

print(a, p, p(1000))
u_x = np.linspace(0, max(y), 1000)

plt.plot(u_x, p(u_x))
plt.plot(y, x, 'or', label='Data')
plt.show()