# Program to multiply two matrices using nested loops
import random
# import line_profiler  

# profiler = LineProfiler()
N = 250

# NxN matrix
@profile
def NN(N):
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    return X
X = NN(N)

# Nx(N+1) matrix

@profile
def N_Nplusone(N):
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    return Y
Y = N_Nplusone(N)


#result is Nx(N+1)
@profile
def NxNplusone(X,Y):
    result = []
    for i in range(N):
        result.append([0] * (N+1))

    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result
result = NxNplusone(X,Y) 
# for r in result:
#     print(r)
