# Program to multiply two matrices using nested loops
import random
import numpy as np
N = 250

# NxN matrix
# X = []
# for i in range(N):
#     X.append([random.randint(0,100) for r in range(N)])

@profile
def NN(N):
    X = np.random.randint(0,100, N)
    return X
X = NN(N)

# Nx(N+1) matrix
# Y = []
# for i in range(N):
#     Y.append([random.randint(0,100) for r in range(N+1)])

# result is Nx(N+1)
@profile
def N_Nplusone(N):
    Y = np.random.randint(0,100,N+1)
    return Y
Y = N_Nplusone(N)
print(X.shape, Y.shape)

@profile
def NxNplusone(X,Y):
    result = np.outer(X,Y)
    return result
result = NxNplusone(X,Y) 
print(result.shape)
# for r in result:
#     print(r)
