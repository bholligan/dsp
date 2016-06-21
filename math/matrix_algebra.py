# Matrix Algebra

import numpy as np

A =  np.matrix([[1,2,3],[2,7,4]])
B =  np.matrix([[1,-1],[0,1]])
C =  np.matrix([[5,-1],[9,1],[6,0]])
D =  np.matrix([[3,-2,-1],[1,2,3]])
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.matrix([[1], [8], [0], [5]])

print("1.1) Dimensions of A are {}".format(A.shape))
print("1.2) Dimensions of B are {}".format(B.shape))
print("1.3) Dimensions of C are {}".format(C.shape))
print("1.4) Dimensions of D are {}".format(D.shape))
print("1.5) Dimensions of u are {}".format(u.size))
print("1.6) Dimensions of w are {}".format(w.shape))

print("2.1) {}".format(u+v))
print("2.2) {}".format(u-v))
print("2.3) {}".format(6*u))
print("2.4) {}".format(np.vdot(u,v)))
print("2.5) {0:.4f}".format(np.linalg.norm(u)))

print("3.1) Not Defined")
print("3.2) {}".format(A-np.transpose(C)))
print("3.3) {}".format(np.transpose(C)+3*D))
print("3.3) {}".format(B*A))
print("3.5) Not Defined")
print("3.6) Not Defined")
print("3.7) {}".format(C*B))
print("3.8) {}".format(B**4))
print("3.9) {}".format(A*np.transpose(A)))
print("3.10) {}".format(np.transpose(D)*D))