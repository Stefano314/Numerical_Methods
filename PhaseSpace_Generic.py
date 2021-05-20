import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spy
import math
from matplotlib import cm #This is for the palet color

#Hamiltonian Systems (Separable):
#   H(q,p) = T(p) + V(q,p)
# ==> dq/dt = H_p(q,p), dp/dt = -H_q(q,p) (solution of motion)
   
#Constants
k = 10
b = 1
NOrbits = 10
time = np.linspace(0, 50, 1001)
q0 = 0
v0 = 5 #This is changing in the loop, so this value doesn't matter.
state = [q0,v0]

def ODE(z,t):
    q,v = z
    zdot = [v, -k*q] #Harmonic Oscillator
    #zdot = [v, 2*q - q**3] #Double well potential
    #zdot = [v, -2*q - 0.1*v] #Damped Harmonic Oscillator   
    #zdot = [v, -q*math.cos(q)] #Casual
    return zdot

colors = cm.jet(np.linspace(0,1,NOrbits))
check = int(input('-Phase space plotting (1) or Motion Plotting (2): '))

if check == 1:
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
elif check == 2:
    #for x0 in range(0,NOrbits):
        #state[1] = x0
    sol = spy.odeint(ODE, state, time)
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(time, sol[:,0], color = colors[0], linestyle = 'dotted')
    ax1.set(xlabel = "time, t", ylabel = "Position, q")
    ax2.plot(time, sol[:,1], color = colors[0], linestyle = 'dotted')
    ax2.set(xlabel = "time, t", ylabel = "Velocity, v")
    fig.suptitle("Motion Solutions")
    fig.show()
else: print("Command not found")
