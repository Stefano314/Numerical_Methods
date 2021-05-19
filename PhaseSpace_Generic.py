import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spy
import math
from matplotlib import cm #This is for the palet color

#Constants
k = 10
b = 1
NOrbits = 10
time = np.linspace(0, 50, 1001)
q0 = 2
v0 = 1. #This is changing in the loop, so this value doesn't matter.
state = [q0,v0]

def ODE(z,t):
    q,v = z
    zdot = [v, 2*q - q**3] #Double well potential
    #zdot = [v, -2*q + 0.1*v] #Damped Harmonic Oscillator   
    #zdot = [v, -q*math.cos(q)] #Casual
    return zdot

colors = plt.cm.jet(np.linspace(0,1,NOrbits))
for x0 in range(0,NOrbits):
    state[1] = x0
    sol = spy.odeint(ODE, state, time)
    plt.plot(sol[:,0],sol[:,1], color = colors[x0], linestyle = 'dotted')
    
plt.xlabel('Position')
plt.ylabel('Velocity')
plt.title('Phase space trajectory')
plt.axhline(linewidth=1, color='r', alpha = 0.8)
plt.axvline(linewidth=1, color='r', alpha = 0.8)
plt.grid(alpha=0.8)
plt.show()
