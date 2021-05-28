import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spy

#=========================== LORENTZ ATTRACTOR ===========================
# Constants
t_max = 50
NPoints = t_max * 100 + 1
time = np.linspace(0, t_max, NPoints)
u0 = 1
v0 = 0.8
w0 = 1.5
ε = 0.0000001
state0 = [u0, v0, w0]
state1 = [u0 + ε, v0 + ε, w0 + ε]

def lorentz(z, t):
    u, v, w = z
    σ = 10
    ρ = 28
    β = 2.6
    zdot = [σ * (v - u), u * (ρ - w) - v, u * v - β * w]
    return zdot

#Numerical Integration
sol0 = spy.odeint(lorentz, state0, time)
sol1 = spy.odeint(lorentz, state1, time)

# Distance plot (Logarithmic Scale)
distance = []
for i in range(0, NPoints):
    distance.append(np.log(np.linalg.norm(sol0[i] - sol1[i])))
plt.plot(time, distance)
plt.title('Logarithmic Distance')
plt.xlabel("Time, t")
plt.ylabel("Distance, log(d)")
plt.show()

# Attractor Plot
fig = plt.figure()
ax = fig.gca(projection = '3d')
#Initial Conditions Highlight
ax.plot(sol0[0, 0], sol0[0, 1], sol0[0, 2], 'o', color = 'aqua', markersize = 5.)
ax.plot(sol1[0, 0], sol1[0, 1], sol1[0, 2], 'o', color = 'coral', markersize = 5.)
ax.set_title('Lorentz Attractor')

# #Solution plot with delay
# for i in range(1, NPoints, 3):
#     ax.plot(sol0[i, 0], sol0[i, 1], sol0[i, 2], 'b.', markersize = 0.9)
#     ax.plot(sol1[i, 0], sol1[i, 1], sol1[i, 2], 'r.', markersize = 0.9)
#     plt.pause(0.01)
# plt.show()

#Solution plot
ax.plot(sol0[:, 0], sol0[:, 1], sol0[:, 2], 'b.', markersize = 0.9)
ax.plot(sol1[:, 0], sol1[:, 1], sol1[:, 2], 'r.', markersize = 0.9)
plt.show()

#===== Taking a point on the attractor and repeat the procedure ====
new_state0 = sol0[NPoints-20] #Careful here, we can go out of indexes.
new_state1 = np.array([new_state0[0]+ε, new_state0[1]+ε, new_state0[2]+ε])

#Numerical Integration
sol0 = spy.odeint(lorentz, new_state0, time)
sol1 = spy.odeint(lorentz, new_state1, time)

# Distance plot (Logarithmic Scale)
distance = []
for i in range(0, NPoints):
    distance.append(np.log(np.linalg.norm(sol0[i] - sol1[i])))
plt.plot(time, distance)
plt.title('Logarithmic Distance')
plt.xlabel("Time, t")
plt.ylabel("Distance, log(d)")
plt.show()

# Attractor Plot
fig = plt.figure()
ax = fig.gca(projection = '3d')
#Initial Conditions Highlight
ax.plot(sol0[0, 0], sol0[0, 1], sol0[0, 2], 'o', color = 'aqua', markersize = 5.)
ax.plot(sol1[0, 0], sol1[0, 1], sol1[0, 2], 'o', color = 'coral', markersize = 5.)
ax.set_title('Lorentz Attractor')

#Solution plot with delay
for i in range(1, NPoints, 3):
    ax.plot(sol0[i, 0], sol0[i, 1], sol0[i, 2], 'b.', markersize = 0.9)
    ax.plot(sol1[i, 0], sol1[i, 1], sol1[i, 2], 'r.', markersize = 0.9)
    plt.pause(0.01)
plt.show()

# #Solution plot
# ax.plot(sol0[:, 0], sol0[:, 1], sol0[:, 2], 'b.', markersize = 0.9)
# ax.plot(sol1[:, 0], sol1[:, 1], sol1[:, 2], 'r.', markersize = 0.9)
# plt.show()
#==================================================================


#=========================== PENDULUM ===========================
# # Constants
# t_max = 10
# NPoints = t_max * 100 + 1
# time = np.linspace(0, t_max, NPoints)
# g = 9.81
# θ0 = 3.14
# ω0 = 0.
# ε = 0.0000001
# state0 = [θ0, ω0]
# state1 = [θ0 + ε, ω0 + ε]

# def Pendulum(z,t):
#     q,v = z
#     zdot = [v, -g*np.sin(q)]
#     return zdot

# #Numerical Integration
# sol0 = spy.odeint(Pendulum, state0, time)
# sol1 = spy.odeint(Pendulum, state1, time)

# # Distance plot (Logarithmic Scale)
# distance = []
# for i in range(0, NPoints):
#     distance.append(np.log(np.linalg.norm(sol0[i] - sol1[i])))
# plt.plot(time, distance)
# plt.title('Logarithmic Distance')
# plt.xlabel("Time, t")
# plt.ylabel("Distance, log(d)")
# plt.show()

# # Pendulum plot
# fig, ax = plt.subplots()
# #Initial Conditions Highlight
# ax.plot(sol0[0, 0], sol0[0, 1], 'o', color = 'aqua', markersize = 5.)
# ax.plot(sol1[0, 0], sol1[0, 1], 'o', color = 'coral', markersize = 5.)
# ax.set_title('Pendulum')

# #Solution plot with delay
# for i in range(1, NPoints, 3):
#     ax.plot(sol0[i, 0], sol0[i, 1], 'b.', markersize = 0.9)
#     ax.plot(sol1[i, 0], sol1[i, 1], 'r.', markersize = 0.9)
#     plt.pause(0.01)
# plt.show()

# # #Solution plot
# # ax.plot(sol0[:, 0], sol0[:, 1], 'b.', markersize = 0.9)
# # ax.plot(sol1[:, 0], sol1[:, 1], 'r.', markersize = 0.9)
# # plt.show()