import numpy as np
from numpy.linalg import *

def trunc(values, decs=0):
    return np.trunc(values*10**decs)/(10**decs)

A = np.matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 255, 255, 0, 0, 0, 0, 0, 255, 255, 0],
               [0, 0, 255, 255, 0, 0, 0, 255, 255, 0, 0],
               [0, 0, 255, 0, 255, 0, 255, 0, 255, 0, 0],
               [0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0],
               [0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0],
               [0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0],
               [0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0],
               [0, 255, 255, 255, 0, 0, 0, 255, 255, 255, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

print(A)
print()

U, s, V = np.linalg.svd(A, full_matrices=False)

img_recon = np.dot(U[:, :5], np.dot(np.diag(s[:5]), V[:5, :]))

U = np.round(U, 2)
V = np.round(V, 2)
img_recon = abs(np.round(img_recon, 3))
# turn img_recon into a matrix of integers
img_recon = img_recon.astype(int)
# turn into a csv
np.savetxt("img_recon.csv", img_recon, delimiter=",", fmt="%d")
np.savetxt("U.csv", U, delimiter=",", fmt="%1.2f")
np.savetxt("V.csv", V, delimiter=",", fmt="%1.2f")

print("U = ")
print(U)
print()
print("s = ")
print(s)
print()
print("V = ")
print(V)
print()
print("Remade: ")
print(img_recon)
