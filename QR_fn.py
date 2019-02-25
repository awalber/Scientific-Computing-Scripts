# This code was written by Aaron Walber for a physics-related scientific 
# computing class at SIUC. It is a QR algorithm that can be iterated
# until a desirable accuracy is met so long as the accuracy and matrix
# A are provided where A is any symmmetric matrix.
from numpy import shape, matrix, sqrt
from numpy.matlib import zeros
def QR(A):
    N = shape(A)[0]
    u,q,R,v = zeros((N,N)),zeros((N,N)),zeros((N,N)),zeros((N,N))
    for j in range(N):
        a = A.transpose()
        for i in range(N):
            v[:,j] += q[:,i]*(a[j,:]@q[:,i])
        u[:,j] = A[:,j] - v[:,j]
        uT = u.transpose()
        q[:,j] = u[:,j]/sqrt((uT[j,:]@u[:,j]))
        Q = q.transpose()
    for k in range(N):
        for m in range(k,N):
            if k == m:
                R[k,m] = sqrt(uT[m,:]@u[:,k])
            else:
                R[k,m] = a[m,:]@q[:,k]
    return q,Q,R