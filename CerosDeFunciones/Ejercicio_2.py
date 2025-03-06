import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
from Biseccion import Biseccion


func = lambda x: (x + np.sqrt(x))* (20 - x + np.sqrt(20-x)) - 155.55

w = np.linspace(0, 20, 1000000)

primer_num = Biseccion(func, 5, 7.5, 1e-5)
segundo_num = Biseccion(func, 12.5, 17.5, 1e-5)

print("Primer numero: ", primer_num)
print("Segundo numero: ", segundo_num)
print("Suma: ", (primer_num[0]+np.sqrt(primer_num[0])) * (segundo_num[0]+np.sqrt(segundo_num[0])),
      "Suma: ", primer_num[0] + segundo_num[0])

plt.plot(w, func(w), 'b')
plt.axhline(0, color='red', linewidth=1, linestyle='dashed')
plt.grid()
plt.show()


