import math
import random

import numpy as np
from lectures import Lectures
from matrixMath import MatrixMath
"""This will be a collection of linear algebra operations.
MATRIX OPERATIONS
ADDITION, SUBTRACTION, """
matrix = MatrixMath()
lectures = Lectures()


A = matrix.randomMatrix(3, 3, -2, 2, int)
print(A)
# Gauss elimination
for i in range(len(A)):
    A[i] = A[i] / A[i][i]
    for l in range(i + 1, len(A)):
        A[l] = A[l] - A[l][i] * A[i]
        #print(i, l)
#print(A)
#print()
for m in range(len(A)-1, -1, -1):
    #print(i)
    for l in range(len(A)-1, m, -1):
        #print(m, l)
        A[m] = A[m] - A[m][l]*A[l]
print()
print(A)
