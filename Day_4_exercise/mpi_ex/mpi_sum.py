import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD 

rank = comm.Get_rank()
size = comm.Get_size()

r = np.array(rank)
# print(r)
summe = 0

if rank > 0:
    # r = rank
    comm.Send(r, dest=0)
    # print(r)
    

if rank == 0:
    for i in range (size-1):
        # print(i)
        comm.Recv(r, source=(i+1))
        summe += r
        # print(r)
    print('The sum of all ranks is ', summe, 'this is prited from rank ', rank)
    
        