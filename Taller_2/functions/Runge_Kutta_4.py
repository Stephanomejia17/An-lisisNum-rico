import numpy as np

def runge_kutta_4(f, a, b, h, y0):
    t_vals = np.linspace(a, b, int((b - a) / h) + 1)
    w_rk4 = [y0]
    
    for i in range(len(t_vals) - 1):
        t = t_vals[i]
        y = w_rk4[i]
        
        k1 = h * np.array(f(t, y))
        k2 = h * np.array(f(t + h/2, y + k1/2))
        k3 = h * np.array(f(t + h/2, y + k2/2))
        k4 = h * np.array(f(t + h, y + k3))
        
        y_next = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        w_rk4.append(y_next)
    
    return t_vals, w_rk4
