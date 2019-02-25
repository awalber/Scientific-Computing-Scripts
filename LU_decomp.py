# This code was written by Aaron Walber for a physics-related scientific 
# computing class at SIUC. It creates an LU decomposition of a matrix where
# L is a lower triangular matrix denoted by the variable temp1 and U is an
# upper triangular matrix denoted by the variable U.
from numpy import shape, matrix, zeros, dot, array
import numpy.matlib
U = matrix('2 1 4 1; 3 4 -1 -1; 1 -4 1 5; 2 -2 1 3',float)
A = matrix('2 1 4 1; 3 4 -1 -1; 1 -4 1 5; 2 -2 1 3',float)
temp = numpy.matlib.zeros((4,4))
N = shape(U)[0]
i,k = 0,0
while i < N:
    L_inverse = matrix('1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1',float)
    L = matrix('1 0 0 0; 0 1 0 0; 0 0 1 0; 0 0 0 1',float)
    while k < N:
        if k >= 1:
            L_inverse[k,i] = -U[k,i]/U[i,i]
        L[k,i] = U[k,i]
        k+=1
    if i >= 1:
        temp1 = dot(temp,L)
        temp = temp1
    else:
        temp = L
        temp[:,i] = A[:,i]
    L_inverse[i,i] = 1/U[i,i]
    U = dot(L_inverse,U)
    i+=1
    k = i
print(U)
print(temp1)
print(dot(temp1,U))