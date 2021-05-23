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
NOrbits = 5
time = np.linspace(0, 50, 1001)
q0 = 2
v0 = 1 #This is changing in the loop.
state = [q0,v0]
def ODE(z,t):
    q,v = z
    #zdot = [v, -k*q] #Harmonic Oscillator
    zdot = [v, 2*q - q**3] #Double well potential
    #zdot = [v, -2*q - 0.1*v] #Damped Harmonic Oscillator   
    #zdot = [v, -q*math.cos(q)] #Casual
    #zdot = [0.6*q - 1.2*q*v, q*v - v]#Lotka-Volterra (q = prey, v = predators)
    return zdot

colors = cm.jet(np.linspace(0,1,NOrbits))
check = int(input('-Phase space plotting (1) or Motion Plotting (2): '))
if check == 1:
    for x0 in range(0,NOrbits):
        state[1] = x0
        sol = spy.odeint(ODE, state, time)
        #======= Label Generation ========
        if x0 == 0: Label = 'E_min'
        elif x0 == NOrbits-1: Label = 'E_max'
        else: Label = str()
        #=================================
        plt.plot(sol[:,0],sol[:,1], color = colors[x0], 
                 linestyle = 'dotted', label = Label)
        plt.plot(sol[0,0],sol[0,1], color = colors[x0], 
                 marker = 'o') #Highlight initial condition
        plt.arrow(sol[0,0], sol[0,1], sol[2,0]-sol[0,0], sol[2,1]-sol[0,1],
              head_width=0.2, color = colors[x0], length_includes_head=True)
    plt.xlabel('Position, q')
    plt.ylabel('Velocity, v')
    plt.title('Phase space trajectory')
    plt.axhline(linewidth=1, color='r', alpha = 0.8)
    plt.axvline(linewidth=1, color='r', alpha = 0.8)
    plt.grid(alpha=0.8)
    plt.legend()
    plt.show()
elif check == 2:
    sol = spy.odeint(ODE, state, time)
    fig, (ax1, ax2) = plt.subplots(2)
    ax1.plot(time, sol[:,0], color = colors[0], linestyle = 'dotted')
    ax1.set(xlabel = "time, t", ylabel = "Position, q")
    ax2.plot(time, sol[:,1], color = colors[0], linestyle = 'dotted')
    ax2.set(xlabel = "time, t", ylabel = "Velocity, v")
    fig.suptitle("Motion Solutions")
    fig.show()
else: print("Command not found")
