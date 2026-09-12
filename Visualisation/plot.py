import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.spatial.transform import Rotation as R

import Simulator.simulator as sim
import Dynamics.parameters

# plt.plot(sim.solution.t, sim.solution.y[0])
# plt.show()

# plt.scatter(sim.solution.y[2], sim.solution.y[0])
# plt.show()

Nt = sim.Nt
t_end = sim.t_end
interval = t_end/(Nt)

t = sim.solution.t*2
x = sim.solution.y[0]      
y = sim.solution.y[1]
z = sim.solution.y[2]      
phi = sim.solution.y[6]
theta = sim.solution.y[7]  
psi = sim.solution.y[8]

# L = Dynamics.parameters.LENGTH  # half-length of the drone body
L = 0.25

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

line1, = ax.plot([], [], [], lw=2, color='blue')
line2, = ax.plot([], [], [], lw=2, color='green')
point, = ax.plot([], [], [], 'ko', markersize=2)
target, = ax.plot([], [], [], 'r*', markersize=15)

# body-frame arm endpoints, before rotation
arm1 = np.array([[ L,  L, 0], [-L, -L, 0]])  # diagonal 1
arm2 = np.array([[ L, -L, 0], [-L,  L, 0]])  # diagonal 2

max = np.max([x.max(),y.max()])
min = np.min([x.min(), y.min()])

ax.set_xlim3d(min-1, max+1)
ax.set_ylim3d(min-1, max+1)
ax.set_zlim3d(z.min()-1, z.max()+1)

def update(frame):
    cx, cy, cz = x[frame], y[frame], z[frame]
    cphi, ctheta, cpsi = phi[frame], theta[frame], psi[frame]

    rot = R.from_euler('ZYX', [cpsi, ctheta, -cphi]).as_matrix()

    world_arm1 = (rot @ arm1.T).T + [cx, cy, cz]
    world_arm2 = (rot @ arm2.T).T + [cx, cy, cz]

    line1.set_data_3d(world_arm1[:, 0], world_arm1[:, 1], world_arm1[:, 2])
    line2.set_data_3d(world_arm2[:, 0], world_arm2[:, 1], world_arm2[:, 2])
    point.set_data_3d([cx], [cy], [cz])

    if frame >= 2* len(t)/3:
        target.set_data_3d([Dynamics.parameters.TARGET_X3], [Dynamics.parameters.TARGET_Y3], [Dynamics.parameters.TARGET_HEIGHT3])

    elif frame >= len(t)/3:
        target.set_data_3d([Dynamics.parameters.TARGET_X2], [Dynamics.parameters.TARGET_Y2], [Dynamics.parameters.TARGET_HEIGHT2])

    else:
        target.set_data_3d([Dynamics.parameters.TARGET_X1], [Dynamics.parameters.TARGET_Y1], [Dynamics.parameters.TARGET_HEIGHT1])

    return line1, line2, point

ani = animation.FuncAnimation(
    fig, update, frames=len(x), interval=80, blit=False
)
ax.view_init(elev=15, azim=-40)
# ani.save('demo_3.gif', writer='pillow', fps=12)
plt.show()