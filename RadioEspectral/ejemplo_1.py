import numpy as np

A = np.array([[-1,2,0], [2,-3,1], [0,1,2]])
l, v = np.linalg.eig(A)

print("lambda 1: ", l[0], "lambda 2: ", l[1], "lambda 3: ", l[2])

radio_esp = max(abs(l))
print("Radio Espectral\n", radio_esp)