import sympy as sp 
import numpy as np

def progresiva(f, x0, h):
    return (f(x0+h) - f(x0))/h