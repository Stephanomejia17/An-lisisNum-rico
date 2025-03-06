import sympy as sp 
import numpy as np

def progresiva(f, x, h):
    return (f(x) - f(x-h))/h