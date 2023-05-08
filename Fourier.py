import math
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

x = np.linspace(0, 10, 999)
y = x

def s(x, y, n):
    
    p = x[-1] - x[0]
    dx = x[1] - x[0]
    
    
    rs = 0
    for i in y:
        rs += i
        
    a0 = (1/p)*rs*dx
    

    l = 0
    z = []
    
    for i in y:
        
        c = 0
        
        for j in range(1, n+1):
            
            an = 0
            bn = 0
            m = 0
            
            for k in y:
                                
                an += (2/p)*k*np.cos((2*np.pi*j*x[m])/p)*dx
                bn += (2/p)*k*np.sin((2*np.pi*j*x[m])/p)*dx
                m += 1            

            c += (an * np.cos((2*np.pi*j*x[l])/p) + bn * np.sin((2*np.pi*j*x[l])/p))
        
        
        z.append(a0 + c)
        l += 1

    return z

s = s(x, y, 30)
