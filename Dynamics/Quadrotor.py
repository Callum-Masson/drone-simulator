import numpy as np

from . import parameters
from Control.pid import thrust

m = parameters.MASS
g = parameters.GRAVITY
L = parameters.LENGTH
I = parameters.IYY




def dynamics(t, state):
    
    if t < 5:
        x_target = parameters.TARGET_X1
        z_target = parameters.TARGET_HEIGHT1

    else:
        x_target = parameters.TARGET_X2
        z_target = parameters.TARGET_HEIGHT2

        


    t1,t2 = thrust(state, x_target, z_target)
    dzdt = state[1]
    dwdt = ((t1 + t2)*np.cos(state[4]) - m*g)/m

    dxdt = state[3]
    dudt = -(t1 + t2)*np.sin(state[4])/m

    dthetadt = state[5]
    dthetadotdt = (t2*L-t1*L)/I



    return [dzdt, dwdt, dxdt, dudt, dthetadt, dthetadotdt]