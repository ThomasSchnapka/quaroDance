#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Helper functions to plot and in this way validate trajectories
"""

import numpy as np
import matplotlib.pyplot as plt
import trajectories as traj
import zero_moment_point as zmp

#N = 200
N = 20
t = np.linspace(0, 2, N)
leg_pos = np.array([[0.2, 0.2, -0.2, -0.2],
                    [0.1, -0.1, 0.1, -0.1],
                    [0, 0, 0, 0]])

x = traj.get_x_trot(t) + np.tile(leg_pos[0], (N, 1)).T
y = traj.get_y_trot(t) + np.tile(leg_pos[1], (N, 1)).T
z = traj.get_z_trot(t) + np.tile(leg_pos[2], (N, 1)).T
leg_state = traj.get_legstate_trot(t)

# desired COP is mean of leg points
p = np.zeros((2, N))
for n in range(N):
    p[0, n] = np.sum(x[leg_state[n], n])/np.sum(leg_state[n])
    p[1, n] = np.sum(y[leg_state[n], n])/np.sum(leg_state[n])
    
p_zmp = zmp.get_zmp(p)

### Plot ####################################################################
fig, (axx, axz) = plt.subplots(2, 1)
fig.set_figheight(10)
fig.set_figwidth(10)

for n in range(4):
    axx.plot(x[n], y[n], label=('x'+str(n)))
    axz.plot(t, x[n])
    axz.plot(t, p_zmp[0])

axx.plot(p_zmp[0], p_zmp[1], label="ZMP")   
axx.plot(p[0], p[1], label="COM")

# plot a single locus
#M = 1
#for n in range(4):
#    axz.plot(x[n, M], y[n, M], "o", label=('x'+str(n)))
#axz.plot(p[0, M], p[1, M], "o", label="COM")
    
axx.legend()
axx.axis('equal')
axz.legend()
axz.axis('equal')
    
