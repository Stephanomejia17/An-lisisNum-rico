import numpy as np

def MinimosCuadrados (x: np.array, y: np.array):
    Sx = sum(x)
    Sy = sum(y)
    Sx2 = sum(x**2)
    Sxy = sum(x*y)
    n = len(x)
    
    return ((Sy * Sx2) - (Sx * Sxy)) / (n * Sx2 - Sx**2), (n * Sxy - Sx * Sy) / (n * Sx2 - Sx**2)