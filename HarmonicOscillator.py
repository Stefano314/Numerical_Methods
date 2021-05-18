import numpy as np
import matplotlib.pyplot as plt

#Oscillator: 
#    dx/dt = v
#    dv/dt = a = -k*x

#Constants
k = 10.
tMax = 5.
q0 = 0.
v0 = 10.
state = [q0,v0]
NPoints = 200
NOrbits = 20 #Number of orbits to plot
inc = (tMax)/NPoints

def rk4(F,x,t,τ):
    K0 = τ*F(x,t)
    K1 = τ*F(x + τ/2.0, t + K0/2.0)
    K2 = τ*F(x + τ/2.0, t + K1/2.0)
    K3 = τ*F(x + τ, t + K2)
    return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0

def euler(F,x,t,τ):
    return τ*F(x,t)

def a_(q,t):
    return -k*q
def v_(v,t):
    return v

def Integrate(state,inc):
    Q = []
    V = []
    q = state[0]
    v = state[1]
    Q.append(q)
    V.append(v)
    for t in np.linspace(0,tMax,NPoints):
        q = q + rk4(v_,v,t,inc)
        v = v + rk4(a_,q,t,inc)
        Q.append(q)
        V.append(v)
    return Q,V

#Generation of the orbits Q_, V_
for x0 in range(0,NOrbits):
    state[0] = x0
    Q_ ,V_ = Integrate(state, inc)
    plt.plot(Q_, V_, color = 'blue', linestyle = 'dotted')

plt.xlabel('Position')
plt.ylabel('Velocity')
plt.title('Phase space trajectory')
plt.axhline(linewidth=1, color='r', alpha = 0.8)
plt.axvline(linewidth=1, color='r', alpha = 0.8)
plt.grid(alpha=0.8)
plt.show()
