import math
import sympy as sym
import matplotlib.pyplot as plt
import numpy as np
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

fig, axs = plt.subplots()
axs.clear()

## Variables that define the wave
start = -10
end = 10
period = 5
steps_per_period = 57   ##This can't go below 4
                        ## It is possible to program functionality for 3 steps per period
                        ## But it isn't prctical to impliment here
stepnumber = (steps_per_period * period) + 1
amplitude = 4
direction = 0
##

def sawchomper(start, end, stepnumber, period, amplitude, direction):
    x = np.linspace(start, end, stepnumber)
    y = []
    Nst = (stepnumber - 1)
#     step = (end - start)/ Nst
    
    v = (Nst / period)
    if v % 2 != 1:
        v+=1
    inc = amplitude / ((v-1)/2)
        
#     print(v)    ## Uncomment for debug
#     print(Nst)
    
    if direction == 0:
        j = 0
        l = 0
        m = 0
        for i in x:
#             print(l)    ## Uncomment for debug
            if l == 0:
                y.append(j)
                j += inc
                l += 1
                m = 0
            elif l <= (v-1)/2:
                y.append(j)
                j += inc
                l += 1
            elif l > (v-1)/2 and l < (v-1):
            ##elif l > (v-1)/2 and l <= (v-1):  ##first step to 3 step functionality
                if m == 0:
                    j = -amplitude
                    m += 1
                y.append(j)
                j += inc
                l += 1
            else:     
                y.append(j)
                j += inc
                l = 0
            
            
    elif direction == 1:
        j = 0
        l = 0
        m = 0
        for i in x:
            if l == 0:
                y.append(j)
                j -= inc
                l += 1
                m = 0
            elif l <= (v-1)/2:
                y.append(j)
                j -= inc
                l += 1
            elif l > (v-1)/2 and l < (v-1):
            ##elif l > (v-1)/2 and l <= (v-1):  ##uncomment to add 3 step functionality
                if m == 0:
                    j = amplitude
                    m += 1
                y.append(j)
                j -= inc
                l += 1
            else:     
                y.append(j)
                j -= inc
                l = 0
                
    return x, y
        
x, y = sawchomper(start, end, stepnumber, period, amplitude, direction)
axs.plot(x, y)

# print(x)    ## Uncomment for debug
# print(y)
