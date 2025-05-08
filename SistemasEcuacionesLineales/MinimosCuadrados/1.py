import numpy as np
import matplotlib.pyplot as plt
from MinimosCuadrados import MinimosCuadrados

x = np.array([0, 2, 3, 6, 7])
y = np.array([0.12, 0.153, 0.17, 0.225, 0.26])


a = MinimosCuadrados(x, y)

print(a)

P_x = lambda x:  a[0] + a[1]*x
u_x = np.linspace(0, max(x), 1000)

plt.plot(u_x, P_x(u_x))
plt.plot(x,y, 'or', label='Data')
plt.legend()
plt.show()
