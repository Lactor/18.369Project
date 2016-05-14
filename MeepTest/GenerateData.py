import os
import numpy as np


fcen = 0.82
df = 0.03
sourcex = -0.2
sourcey = -0.1
Ez = 'true'
single_mode = 'true'

Corners = [np.array([-0.054, 0.02]),
           np.array([-0.044, 0.02]),
           np.array([-0.044, -0.02]),
           np.array([-0.054, -0.02]),
           np.array([-0.054, 0.02])]

n = [6,5,6,5]
ny = 5

# Generate points in k space
k = []

for l in range(4):
    dc = (Corners[l+1]- Corners[l])/(n[l]-1) 
    for i in range(n[l]-1):
        k.append(Corners[l] + i*dc)
    
print k
        
for kpoint in k:
    
    command = "meep fcen=%.2f df=%.2f sourcex=%.2f sourcez=%.2f Ez?=%s single-mode?=%s targetkx=%.3f targetky=%.3f Mode.ctl > kx_%.3fky_%.3f.out" % ( fcen, df, sourcex, sourcey, Ez, single_mode, kpoint[0], kpoint[1], kpoint[0], kpoint[1])
    
    print "RUNNING:"
    print command
    print ""
    os.system(command)
