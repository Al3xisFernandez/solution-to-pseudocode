#!/usr/bin/env python
# coding: utf-8

# In[2]:
#function puzzle(N) {
#.A = 1
#.B = 1
#.C = 1
#.D = 1
#.repeat N times {
#....X = D + 2 * C + 3 * B + 4 * A
#....A = B
#....B = C
#....C = D
#....D = X
#.}
#return D % 10000000000 // últimos 10 dígitos de D
# }
# print puzzle(10)
# rint puzzle(100)
# print puzzle(pow(2022, 100)) // 2022 elevado a la 100
# (los puntos son para identación)
# ====== Output ======
# 30520
# 720820623
# ???
import numpy as np
def multiply_matrix(A, B, mod):
  global C
  if A.shape[1] == B.shape[0]:
    C = np.zeros((A.shape[0], B.shape[1]), dtype='int64')
    for row in range(A.shape[0]):
        for col in range(B.shape[1]):
            for elt in range(B.shape[0]):
              C[row, col] = (C[row, col] + A[row, elt] * B[elt, col]) % mod
    return C
  else:
    return "Sorry, cannot multiply A and B."
def exponentiation(base, exp, N):
    result = np.identity(base.shape[0]);
    while exp > 0:
        # If power is oddLL
        if exp % 2 == 1:
            result = multiply_matrix(result,  base, N);
        # Divide the power by 2
        exp = exp // 2
        # Multiply base to itself
        base = multiply_matrix(base, base, N);
    return result;
def puzzle(i):
    N = 1000000000;
    A = np.asmatrix(np.array([[1, 2, 3, 4],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]]));
    B = np.asmatrix(np.array([[1], [1], [1], [1]]));
    C = multiply_matrix(exponentiation(A, i, N), B, N);
    return C[0][0];
print(puzzle(10))
print(puzzle(100))
print(puzzle(pow(2022, 100)))


# %%
