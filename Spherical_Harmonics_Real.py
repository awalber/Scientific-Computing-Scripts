# This code was written by Aaron Walber for a Mathematical 
# Methods class at SIUC. It visualizes the real portion of
# the spherical harmonic where l = 7 and m = 3
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

# Here, I set the coefficient of this particular spherical harmonic as A.
# The calculation was done on paper to avoid computing a derivative numerically.
# I also set the number of points to plot as N.
A = .002069
N = 25

def Re(x,y):
    return A*np.cos(3*y)*(-13440*np.sin(x)**3+36960*np.sin(x)**5-24024*np.sin(x)**7)
theta, phi = np.linspace(0, 2 * np.pi, N), np.linspace(0, np.pi, N)
THETA, PHI = np.meshgrid(theta, phi)
R_Re = Re(THETA,PHI)
X_Re = R_Re * np.sin(PHI) * np.cos(THETA)
Y_Re = R_Re * np.sin(PHI) * np.sin(THETA)
Z_Re = R_Re * np.cos(PHI)
fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
plot = ax.plot_surface(
    X_Re, Y_Re, Z_Re, rstride=1, cstride=1, cmap=plt.get_cmap('CMRmap'),
    linewidth=2, antialiased=False, alpha=0.4)
plt.show()