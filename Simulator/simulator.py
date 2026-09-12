import numpy as np
from scipy.integrate import solve_ivp

from Dynamics.Quadrotor import dynamics


class State():
    def __init__(self, x, y, z, vx, vy, vz, phi, theta, psi, p, q, r):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.phi = phi
        self.theta = theta
        self.psi = psi
        self.p = p
        self.q = q
        self.r = r

t_end = 20
Nt = 45000
        

initial_state = State(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


solution = solve_ivp(
    dynamics, 
    [0,t_end], 
    [
        initial_state.x,
        initial_state.y,
        initial_state.z,
        initial_state.vx,
        initial_state.vy,
        initial_state.vz,
        initial_state.phi,
        initial_state.theta,
        initial_state.psi,
        initial_state.p,
        initial_state.q,
        initial_state.r
    ],
    t_eval= np.linspace(0, t_end, 250)
    )

