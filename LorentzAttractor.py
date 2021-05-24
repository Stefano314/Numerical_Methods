import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spy

# Constants
t_max = 50
NPoints = t_max * 100 + 1
time = np.linspace(0, t_max, NPoints)
u0 = 0
v0 = 1
w0 = 1.5
ε = 0.1
state0 = [u0, v0, w0]
state1 = [u0 + ε, v0 + ε, w0 + ε]

def lorentz(z, t):
    u, v, w = z
    σ = 10
    ρ = 28
    β = 2.6
    zdot = [σ * (v - u), u * (ρ - w) - v, u * v - β * w]
    return zdot

sol0 = spy.odeint(lorentz, state0, time)
sol1 = spy.odeint(lorentz, state1, time)
d = []
for i in range(0, NPoints):
    d.append(np.linalg.norm(sol0[i] - sol1[i]))

# Distance plot
plt.plot(time, d)
plt.show()
# Attractor Plot
fig = plt.figure()
ax = fig.gca(projection = '3d')
for i in range(1, NPoints):
    ax.plot(sol0[3*i, 0], sol0[3*i, 1], sol0[3*i, 2], 'b.', markersize=0.9)
    ax.plot(sol1[3*i, 0], sol1[3*i, 1], sol1[3*i, 2], 'r.', markersize=0.9)
    plt.pause(0.01)
# ax.plot(sol0[:, 0], sol0[:, 1], sol0[:, 2], 'b.', markersize=0.9)
# ax.plot(sol1[:, 0], sol1[:, 1], sol1[:, 2], 'r.', markersize=0.9)
plt.plot(sol0[0, 0], sol0[0, 1], sol0[0, 2], 'bo')
plt.plot(sol1[0, 0], sol1[0, 1], sol1[0, 2], 'ro', )
plt.title('Lorentz Attractor')
plt.show()