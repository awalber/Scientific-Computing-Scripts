#This code was written by Aaron Walber, visualizes the
#electric field and equipotential field lines for the
#analytic function f(z) = z^3
import pylab as pl
import numpy as np

def f(x,y):
    return (x/pl.cos(3*y))**(1/3)
def g(x,y):
    return (x/pl.sin(3*y))**(1/3)

#scale factor used to create a more accurate representation
#of the field lines by creating a larger theta array
sf = 1000
#Values for the real and imaginary components
#(u and v respectively) of the analytic function 
u = [-10,-1,-.1,0,.1,1,10]

theta = pl.arange(-np.pi,np.pi,np.pi/sf)
pl.subplot(111,projection = 'polar')
for i in range(len(u)):
    r = f(u[i],theta)
    R = g(u[i],theta)
    pl.plot(theta,R, color = 'blue')
    pl.plot(theta,r, color = 'red')

pl.xticks(np.arange(0,np.pi*2,np.pi/4),('0',r'$\frac{\pi}{4}$',\
    r'$\frac{\pi}{2}$',r'$\frac{3\pi}{4}$',r'$\pi$',\
    r'$\frac{5\pi}{4}$',r'$\frac{3\pi}{2}$',r'$\frac{7\pi}{4}$'))
pl.yticks(np.arange(0,4.1,2))
pl.ylim([0,4])
pl.show()