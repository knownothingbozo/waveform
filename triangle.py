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
steps_per_period = 99   ##This can't go below 4
                        ## If this value is not divisible by four the waveform will not end in one full cycle
stepnumber = (steps_per_period * period) + 1
amplitude = 4
direction = 1
##

def sawchomper(start, end, stepnumber, period, amplitude, direction):
    x = np.linspace(start, end, stepnumber)
    y = []
#     print(x)
    Nst = (stepnumber - 1)
#     step = (end - start)/ Nst
    
    v = (Nst / period)
    while v % 4 != 0:
        v+=1
    inc = amplitude / (v/4)
        
#     print(v)    ## Uncomment for debug
#     print(Nst)
    
    if direction == 0:
        j = 0
        l = 0
        for i in x:
#             print(l)    ## Uncomment for debug
            if l == 0:
                y.append(j)
                l += 1
            elif l <= v/4:
                j += inc
                y.append(j)
                l += 1
            elif l == (v-1) and l == v/2 + v/4:
                j -= inc
                y.append(j)
                l=0
                j=0
            elif l > v/4 and l <= v/2 + v/4:
                j -= inc
                y.append(j)
                l += 1
            elif l > v/2 + v/4 and l < (v-1):
                j += inc
                y.append(j)
                l += 1
            elif l == (v-1):
                j += inc
                y.append(j)
                l=0
                j=0
            
            
    elif direction == 1:
        j = 0
        l = 0
        m = 0
        for i in x:
#             print(l)    ## Uncomment for debug
            if l == 0:
                y.append(j)
                l += 1
            elif l <= v/4:
                j -= inc
                y.append(j)
                l += 1
            elif l == (v-1) and l == v/2 + v/4:
                j += inc
                y.append(j)
                l=0
                j=0
            elif l > v/4 and l <= v/2 + v/4:
                j += inc
                y.append(j)
                l += 1
            elif l > v/2 + v/4 and l < (v-1):
                j -= inc
                y.append(j)
                l += 1
            elif l == (v-1):
                j -= inc
                y.append(j)
                l=0
                j=0
                
    return x, y
        
x, y = sawchomper(start, end, stepnumber, period, amplitude, direction)
axs.plot(x, y)

# print(x)    ## Uncomment for debug
# print(y)
#
