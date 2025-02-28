import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import pandas as pd

h=0.1
c=15
g=9.8
masa=68.1

t=[0]
x=[0]
v_analitica = [0]
m=68.1
switch = 0
info = [[0,0,0,0]]
t_impacto = 0

while True:
    if t[-1] >= 3000:
        break
    else:
        x.append(h*(g-(c/m)*x[-1])+x[-1])
        if ((round(x[-1], 2) - round(x[-2], 2)) == 0) and switch == 0:
            t_impacto = t[-1]
            switch = 1
        t.append(t[-1]+h)
        v_analitica.append(((g*m)/c)*(1 - np.exp(-(c/m)*t[-1])))
        
        error_abs = np.abs(v_analitica[-1] - x[-1])


        info.append([t[-1], x[-1], v_analitica[-1], error_abs])
        
        

        
d = pd.DataFrame(data=info, columns=['Tiempo (s)', 'Velocidad Aproximada (m/s)', 'Velocidad Analítica (m/s)', 'Error Absoluto'])

print(d)
print("Aproximadamente el paracaidista se impactó a los ", t_impacto, " segundos")

fig, ax = plt.subplots(3, 1, figsize=(8, 6))  # 2 filas, 1 columna

ax[0].plot(d["Tiempo (s)"], d["Velocidad Aproximada (m/s)"], label="Aproximada", color="b")
ax[0].set_title("Velocidad Aproximada vs Tiempo")
ax[0].set_xlabel("Tiempo (s)")
ax[0].set_ylabel("Velocidad (m/s)")
ax[0].grid()
ax[0].legend()

ax[1].plot(d["Tiempo (s)"], d["Velocidad Analítica (m/s)"], label="Analítica", color="r")
ax[1].set_title("Velocidad Analítica vs Tiempo")
ax[1].set_xlabel("Tiempo (s)")
ax[1].set_ylabel("Velocidad (m/s)")
ax[1].grid()
ax[1].legend()

ax[2].plot(d["Tiempo (s)"], d["Error Absoluto"], label="Absoluto", color="g")
ax[2].set_title("Error Absoluto vs Tiempo")
ax[2].set_xlabel("Tiempo (s)")
ax[2].set_ylabel("Error Absoluto")
ax[2].grid()
ax[2].legend()

plt.tight_layout()

plt.show()
