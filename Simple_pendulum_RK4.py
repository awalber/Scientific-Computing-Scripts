# This code was written by Aaron Walber for a physics-related scientific 
# computing class at SIUC. It solves the differential equation for a simple
# pendulum using the Runge-Kutta method of integration.
import pylab as pl
import numpy as np
import matplotlib as mpl

def f(r,t):
    theta = r[0]
    omega = r[1]
    f_omega = -(g/l)*np.sin(theta)
    f_theta = omega
    return np.array([f_theta,f_omega],float)
# Set the variables to be used in the problem. Here, g is the
# acceleration due to gravity and l is the length of the string
# the pendulum is hanging from. Although not integral to solving
# the problem, you can assume SI units (kg, m, s)
g,l = 9.8,.1
# a, b, N are set as initial time, final time, and number of points
# the respective time difference will be divided into, which is h.
a,b,N = 0.0,10.0,10000
h = (b-a)/N
theta = []
omega = []
r = np.array([np.pi/4,0])
T = pl.arange(a,b,h)
for t in T:
    theta.append(r[0])
    omega.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+.5*k1,t+.5*h)
    k3 = h*f(r+.5*k2,t+.5*h)
    k4 = h*f(r+k3,t+h)
    r = r + (k1+2*k2+2*k3+k4)/6
pl.plot(T,theta,'red')
#pl.show()

# A seperate code that evaluates the difference between Runge-Kutta
# and the Euler method of integration requires the line above to be
# commented out.