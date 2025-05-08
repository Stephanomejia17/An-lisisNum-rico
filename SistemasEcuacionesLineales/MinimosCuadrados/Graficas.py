from Lagrange import Lagrange

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from MinimosCuadrados import MinimosCuadrados


def Graficas (x, y):
    var = sp.symbols('x')
    u_x = np.linspace(min(x), max(x), 1000)
    P = sp.lambdify(var, Lagrange(x, y)[1])
    
    plt.plot(x, y, 'or', label='Data')
    plt.legend()
    plt.show()

    plt.figure(figsize=(12,12), dpi=100)

    # grafica x, y
    plt.subplot(3,3,1)    
    plt.plot(x, y, 'or', label='x, y')
    plt.legend()
    # grafica x sqr y
    plt.subplot(3,3,2)
    plt.plot(x, np.sqrt(y), 'or', label='raiz y, x')
    
    plt.legend()
    # Grafica x, 1/y
    plt.subplot(3,3,3)
    plt.plot(x, 1/y, 'or', label='x, 1/y')
    
    plt.legend()
    # Grafica x**2, y
    plt.subplot(3,3,4)
    plt.plot(x**2, y, 'or', label='x**2, y')
    
    plt.legend()
    #Grafica x**3, y
    plt.subplot(3,3,5)
    plt.plot(x**3, y, 'or', label='x**3, y')
    
    plt.legend()
    # Grafica Log x, y    <----------------
    plt.subplot(3,3,6)
    plt.plot(np.log(x), y, 'or', label='Log(x), y')
    
    plt.legend()
    # Grafica x, Log y
    plt.subplot(3,3,7)
    plt.plot(x, np.log(y), 'or', label='x, Log(y)')
    
    plt.legend()
    # Grafica sqr x, y
    plt.subplot(3,3,8)
    plt.plot(np.sqrt(x), y, 'or', label='raiz x, y')
    
    plt.legend()
    # Grafica Log x, Log y
    plt.subplot(3,3,9)
    plt.plot(np.log(x), np.log(y), 'or', label='Log x, Log y')
    
    plt.legend()
    plt.show()