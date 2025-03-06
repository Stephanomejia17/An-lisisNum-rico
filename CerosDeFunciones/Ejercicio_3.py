import matplotlib.pyplot as plt
import sympy as sp
import numpy as np
from Biseccion import Biseccion


func = lambda x: x**10 -1 

bisecc = Biseccion(func, 0, 1.5, 1e-6)
print(bisecc)