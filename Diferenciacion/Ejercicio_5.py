import numpy as np
import matplotlib.pyplot as plt

c = 10
k = .25
h = 0.1

f = -k*c*h+c
res = [c]
t = [0]
i = 0
horas = 0
while i < 0.9:
    
    res.append(-k*res[-1]*h + res[-1])
    
    i += h
    t.append(t[-1] + h)
    
for i in range(0, len(res)):
    print("Concentración en ", round(horas, 1), " horas: ", res[i])
    horas += 2.4
   
plt.plot(t, res)
plt.grid()
plt.show()