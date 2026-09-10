import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

import Simulator.simulator as sim
import Dynamics.parameters

# plt.plot(sim.solution.t, sim.solution.y[0])
# plt.show()

# plt.scatter(sim.solution.y[2], sim.solution.y[0])
# plt.show()

t = sim.solution.t
x = sim.solution.y[2]      # x position
z = sim.solution.y[0]      # z position (adjust index to match your state vector)
theta = sim.solution.y[4]  # pitch angle (adjust index to match your state vector)

# L = Dynamics.parameters.LENGTH  # half-length of the drone body
L = 0.5

fig, ax = plt.subplots()
ax.set_xlim(x.min() - 1, x.max()+1)
ax.set_ylim(z.min() - 1, z.max()+1)
ax.set_aspect('equal')
ax.set_xlabel("x (m)")
ax.set_ylabel("z (m)")

line, = ax.plot([], [], lw=1, color='black')
point, = ax.plot([], [], 'ro', markersize=8)

def update(frame):
    cx = x[frame]
    cz = z[frame]
    ang = theta[frame]

    dx = L * np.cos(ang)
    dz = L * np.sin(ang)

    x_data = [cx - dx, cx + dx]
    z_data = [cz - dz, cz + dz]

    line.set_data(x_data, z_data)
    if frame < len(t)/4:
        point.set_data([Dynamics.parameters.TARGET_X1], [Dynamics.parameters.TARGET_HEIGHT1])

    else:
        point.set_data([Dynamics.parameters.TARGET_X2], [Dynamics.parameters.TARGET_HEIGHT2])
    return line,

interval_ms = (t[1] - t[0]) * 1000
    

ani = animation.FuncAnimation(
    fig, update, frames=len(t), interval=20, blit=False
)

# ani.save('demo_3.gif', writer='pillow', fps=30)

plt.show()