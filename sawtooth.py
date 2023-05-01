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
end = 10
period = 2 
steps_per_period = 4   ##This can't go below 4
                        ## It is possible to program functionality for 3 steps per period
                        ## Uncomment below to implement
stepnumber = (steps_per_period * period) + 1
amplitude = 2
direction = 1
##

def sawchomper(start, end, stepnumber, period, amplitude, direction):
    x = np.linspace(start, end, stepnumber)
    y = []
    Nst = (stepnumber - 1)
    step = (end - start)/ Nst
    v = (Nst / period)
    if v % 2 != 1:
        v+=1
        
    print(v)    ## Uncomment for debug
    print(Nst)
    
    if direction == 1:
        j = 0
        l = 0
        m = 0
        for i in x:
#             print(l)    ## Uncomment for debug
            if l == 0:
                y.append(j)
                j += step
                l += 1
                m = 0
            elif l <= (v-1)/2:
                y.append(j)
                j += step
                l += 1
            elif l > (v-1)/2 and l < (v-1):
            ##elif l > (v-1)/2 and l <= (v-1):  ##uncomment to add 3 step functionality
                if m == 0:
                    j = -step*(v-1)/2
                    m += 1
                y.append(j)
                j += step
                l += 1
            else:     
                y.append(j)
                j += step
                l = 0
            
            
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

print(x)    ## Uncomment for debug
print(y)
