#!/usr/bin/python

# Program to multiply two matrices using nested loops
import numpy as np
import random
# import line_profiler
# profile = line_profiler.LineProfiler()


N = 250

# NxN matrix
@profile
def MultiplyMatrix(N):
    X = np.random.randint(0,100,N*N).reshape(N,N)
    Y = np.random.randint(0,100,N*(N+1)).reshape(N,N+1)
    result = np.matmul(X,Y)
        

    print(result)
    # for r in result:
    #     print(r)
    return result

x = MultiplyMatrix(N)
