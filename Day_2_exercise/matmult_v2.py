#!/usr/bin/python

# Program to multiply two matrices using nested loops
import random
#import line_profiler
#profile = line_profiler.LineProfiler()


N = 5

# NxN matrix
@profile
def MultiplyMatrix(N):
    X = []
    Y = []
    result = []
    
    
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
        Y.append([random.randint(0,100) for r in range(N+1)])
        result.append([0] * (N+1))
        # print(result)
        
    
    # iterate through rows of X
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    
    for r in result:
        print(r)
    return result

x = MultiplyMatrix(N)
