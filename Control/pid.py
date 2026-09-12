import numpy as np

import Dynamics.parameters

m = Dynamics.parameters.MASS
g = Dynamics.parameters.GRAVITY
max_thrust = Dynamics.parameters.MAX_THRUST

Kpx = 0.4
Kdx = 0.2
Kpy = 0.4
Kdy = 0.2
Kptheta = 50
Kdtheta = 10
Kpphi = 50
Kdphi = 10
Kpz = 25
Kdz = 12





def thrust(state, x_target, y_target, z_target):

    ex = x_target - state[0]
    ey = y_target - state[1]
    ez = z_target - state[2]

    evx = 0 - state[3]
    evy = 0 - state[4]
    evz = 0 - state[5]

    desired_phi = np.clip((Kpy*ey + Kdy * evy) * np.cos(state[8]) + (Kpx*ex + Kdx * evx)*np.sin(state[8]), -np.pi/4, np.pi/4)
    desired_theta = np.clip((Kpx*ex + Kdx * evx)*np.cos(state[8]) + (Kpy*ey + Kdy * evy) * np.sin(state[8]), -np.pi/4, np.pi/4)

    etheta = desired_theta - state[7]
    ephi = desired_phi - state[6]

    eq = 0 - state[10]
    ep = 0 - state[9]

    base_thrust = (m*g/4)/(np.cos(state[6]) * np.cos(state[7])) + Kpz * ez + Kdz * evz 

    t1 = base_thrust + ((-Kptheta * etheta - Kdtheta * eq) + (Kpphi * ephi + Kdphi * ep))
    t2 = base_thrust + ((-Kptheta * etheta - Kdtheta * eq) + (-Kpphi * ephi - Kdphi * ep))
    t3 = base_thrust + ((Kptheta * etheta + Kdtheta * eq) + (Kpphi * ephi + Kdphi * ep))
    t4 = base_thrust + ((Kptheta * etheta + Kdtheta * eq) + (-Kpphi * ephi - Kdphi * ep))

    t1 = np.clip(t1,0,max_thrust)
    t2 = np.clip(t2,0,max_thrust)
    t3 = np.clip(t3,0,max_thrust)
    t4 = np.clip(t4,0,max_thrust)

    return t1, t2, t3, t4


