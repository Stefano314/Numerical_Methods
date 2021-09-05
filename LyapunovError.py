import matplotlib.pyplot as plt
import matplotlib.colors as plt_col
import numpy as np
import scipy.integrate as spy

def LE(S, S_eps, t, eps):
    return np.sqrt((S_eps[t,0] - S[t,0])**2 + (S_eps[t,1] - S[t,1])**2 ) / eps

# Constants
NGrid = 200
NPoints = 1001
time = np.linspace(0, 8, NPoints)
q0 = 0.
v0 = 0.
state0 = np.array([q0, v0])
α, β, δ = 1., 1., 0.1
Ɛ = 10 ** (-11)

def ODE(z,t):
    q,v = z
    zdot = [v,  α*q - δ*v - β*q**3]
    return zdot

def err(S, S_eps, t, eps):
    return np.sqrt((S_eps[t,0] - S[t,0])**2 + (S_eps[t,1] - S[t,1])**2 ) / eps

# Perturbative vector generation, outside the loop for performances improvement.
perturb = np.random.uniform(-100, 100, [2])
perturb = Ɛ * perturb / np.linalg.norm(perturb)

#============== GRID SIMULATION ==============
x = [i for i in range(0, NGrid**2)]
y = [i for i in range(0, NGrid**2)]
z = [i for i in range(0, NGrid**2)]
j = 0
for i in range(0,NGrid):
    print(i,'/',NGrid)
    for l in range(0,NGrid):
        state0[0] = - 2. + 4. * i / NGrid
        state0[1] = - 2. + 4. * l / NGrid
        sol = spy.odeint(ODE, state0, time)
        sol_eps = spy.odeint(ODE, state0 + perturb, time)
        error = LE(sol, sol_eps, 900, Ɛ)
        x[j] = state0[0]
        y[j] = state0[1]
        z[j] = error
        j += 1
x = np.array(x)
y = np.array(y)
z = np.array(z)
#=============================================

#================= SAVE DATA =================
# np.save('q.npy', x)
# np.save('p.npy', y)
# np.save('LE_err.npy', z)
#=============================================

#================= DATA PLOT =================
plt.hist2d(x,y, bins = NGrid, range = [[-2.1, 2.1], [-2.1, 2.1]], weights = z, norm = plt_col.LogNorm(), cmap='inferno')
plt.colorbar()
plt.xlabel('Position, q',fontsize=14)
plt.ylabel('Momentum, p',fontsize=14)
plt.title('Lyapunov Error, Duffing Oscillator', fontweight="bold",fontsize=16)
plt.show()
#=============================================
