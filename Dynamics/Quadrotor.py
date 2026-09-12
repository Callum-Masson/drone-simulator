import numpy as np

from . import parameters
from Control.pid import thrust

m = parameters.MASS
g = parameters.GRAVITY
L = parameters.LENGTH
Ix = parameters.IXX
Iy = parameters.IYY
Iz = parameters.IZZ
k = parameters.K






def dynamics(t, state):
    
    if t < 20/3:
        x_target = parameters.TARGET_X1
        y_target = parameters.TARGET_Y1
        z_target = parameters.TARGET_HEIGHT1

    elif t < 40/3:
        x_target = parameters.TARGET_X2
        y_target = parameters.TARGET_Y2
        z_target = parameters.TARGET_HEIGHT2

    else:
        x_target = parameters.TARGET_X3
        y_target = parameters.TARGET_Y3
        z_target = parameters.TARGET_HEIGHT3

        


    t1, t2, t3, t4 = thrust(state, x_target, y_target, z_target)
    tt = t1 + t2 + t3 + t4

    ddt = np.zeros(12)

    ddt[0] = state[3]       #dxdt
    ddt[1] = state[4]       #dydt
    ddt[2] = state[5]       #dzdt

    ddt[3] = (np.sin(state[7])*np.cos(state[6])*np.cos(state[8]) + np.sin(state[8]) * np.sin(state[6]))*tt/m      #dvxdt
    ddt[4] = (np.sin(state[7])*np.cos(state[6])*np.sin(state[8]) + np.cos(state[8]) * np.sin(state[6]))*tt/m      #dvydt
    ddt[5] = np.cos(state[6])*np.cos(state[7]) * tt/m - g       #dwdt

    ddt[6] = state[9] + (state[10]*np.sin(state[6]) + state[11]*np.cos(state[6]))*np.tan(state[7])      #phi dot
    ddt[7] = state[10] * np.cos(state[6]) - state[11] * np.sin(state[6])        #theta dot
    ddt[8] = (state[10] * np.sin(state[6]) + state[11] * np.cos(state[6]))/np.cos(state[7])     #psi dot

    taux = L * np.sin(np.pi/4) * (t1+t3 - (t2+t4))
    tauy = L * np.sin(np.pi/4) * (t3+t4 - (t1+t2))
    tauz = k * (t1 + t4 - t2 - t3)

    ddt[9] = (Iy - Iz)/Ix * state[10] * state[11] + taux/Ix     #p dot
    ddt[10] = (Iz - Ix)/Iy * state[9] * state[11] + tauy/Iy     #q dot
    ddt[11] = (Ix - Iy)/Iz * state[9] * state[10] + tauz/Iz     #r dot


    return ddt