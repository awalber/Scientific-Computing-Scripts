# This code was written by Aaron Walber for a physics-related scientific 
# computing class at SIUC. It solves the differential equation for a simple
# pendulum using the Euler method of integration.
import pylab as pl
import numpy as np
import matplotlib as mpl

def f(r,t):
    theta1 = r1[0]
    omega1 = r1[1]
    f_omega1 = -(g/l)*np.sin(theta1)
    f_theta1 = omega1
    return np.array([f_theta1,f_omega1],float)
# Set the variables to be used in the problem. Here, g is the
# acceleration due to gravity and l is the length of the string
# the pendulum is hanging from. Although not integral to solving
# the problem, you can assume SI units (kg, m, s)
g,l = 9.8,.1
# a, b, N are set as initial time, final time, and number of points
# the respective time difference will be divided into, which is h.
a,b,N = 0.0,10.0,10000
h = (b-a)/N
theta1 = []
omega1 = []
r1 = np.array([np.pi/4,0])
T1 = pl.arange(a,b,h)
for t in T1:
    theta1.append(r1[0])
    omega1.append(r1[1])
    r1 = f(r1,t)*h + r1
pl.plot(T1,theta1,'blue')
#pl.show()

# A seperate code that evaluates the difference between Runge-Kutta
# and the Euler method of integration requires the line above to be
# commented out.
