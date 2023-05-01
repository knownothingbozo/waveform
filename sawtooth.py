import math
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

fig, axs = plt.subplots()
axs.clear()

## Variables that define the wave
start = 0
stepnumber = 15
end = 10
period = 4
amplitude = 2
direction = 1
##

def sawchomper(start, end, stepnumber, period, amplitude, direction):
    x = np.linspace(start, end, stepnumber)
    y = []
    step = (end - start)/ (stepnumber - 1)
    k = start + period/2
    
    if direction == 1:
        j = 0
        for i in x:
            if i < k:
                y.append((j/period) * amplitude)
                j += step
            else:
                
                j = -amplitude
                y.append((j/period) * amplitude)
                j += step
                k += period
                
    elif direction == 0:
        j = period
        for i in x:
            if i < k:
                y.append((j/period) * amplitude)
                j -= step
            else:
                
                j = period
                y.append((j/period) * amplitude)
                j -= step
                k += period
                
    return x, y
        
x, y = sawchomper(start, end, stepnumber, period, amplitude, direction)
axs.plot(x, y)
