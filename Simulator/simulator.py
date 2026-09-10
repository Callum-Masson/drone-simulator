import numpy as np
from scipy.integrate import solve_ivp

from Dynamics.Quadrotor import dynamics


class State():
    def __init__(self, z, w, x, u, th, om):
        self.z = z
        self.w = w
        self.x = x
        self.u = u
        self.th = th
        self.om = om

initial_state = State(0, 0, 0, 0, 0, 0)


solution = solve_ivp(
    dynamics, 
    [0,20], 
    [initial_state.z, initial_state.w, initial_state.x, initial_state.u, initial_state.th, initial_state.om],
    t_eval= np.linspace(0, 20, 1000)
    )

