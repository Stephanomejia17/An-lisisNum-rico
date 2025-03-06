import sympy as sp 
import numpy as np

def progresiva(f, x, h):
    return (f(x+h) - f(x-h))/(2*h)