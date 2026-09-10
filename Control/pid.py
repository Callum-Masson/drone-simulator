import numpy as np

import Dynamics.parameters

m = Dynamics.parameters.MASS
g = Dynamics.parameters.GRAVITY

Kpx = Dynamics.parameters.KP
Kdx = Dynamics.parameters.KD
max_thrust = Dynamics.parameters.MAX_THRUST
Kptheta = 50
Kdtheta = 10
Kpz = 12.5
Kdz = 10
Kpf = 1




def thrust(state, x_target, z_target):
    
    # e = (target - state[0])
    # e_speed = (0 - state[1])

    # thrust = m*g + Kp * e + Kd * e_speed
    # return thrust

    ex = x_target - state[2]
    ez = z_target - state[0]

    eu = 0 - state[3]
    ew = 0 - state[1]

    theta = np.arctan2(ez,ex)

    desired_angle = np.clip(-Kpx*ex - Kdx * eu, -np.pi/2, np.pi/2)

    etheta = desired_angle - state[4]
    eomega = 0 - state[5]

    base_thrust = m*g/2 + Kpz * ez + Kdz * ew + Kpf*abs(state[4])

    t1 = base_thrust - Kptheta * etheta - Kdtheta * eomega
    t2 = base_thrust + Kptheta * etheta + Kdtheta * eomega

    t1 = np.clip(t1,0,max_thrust)
    t2 = np.clip(t2,0,max_thrust)

    

    return t1,t2

