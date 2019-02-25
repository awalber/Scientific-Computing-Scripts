# This code was written by Aaron Walber for a physics-related scientific 
# computing class at SIUC. It initializes the script QR_fn.py with a specific
# symmetric matrix 'A' in order to find the eigenvalues of A to a certain
# accuracy set by the variable 'error'.
from Custom_Projects.Linear_alg.QR_fn import QR
from numpy import tril, triu, diag, matrix

# The function QR returns Q as (QR(A)[0]), Q transpose as (QR(A)[1]), 
# and R as (QR(A)[2])
A = matrix('1 4 8 4; 4 2 3 7; 8 3 6 9; 4 7 9 2 ',float)
error = .0000001
while (tril(A,-1)+triu(A,1)).max() > error:
    A = QR(A)[1]@A@QR(A)[0]

# Printing A shows the entire matrix where every off-diagonal value
# is zero to an accuracy set by 'error'
print(A)

# Printing the diagonal of A simply shows the eigenvalues of A
print(diag(A))