"""
R-5.8 Experimentally evaluate the efficiency of the pop method of Python’s list
class when using varying indices as a parameter, as we did for insert on
page 205. Report your results akin to Table 5.5.
"""

import time
from random import randint

def pop_performance(N):
    for n in N:
        A = [randint(0, 65563) for _ in range(0, n)]
        for k in [0, len(A) // 2, len(A)-1]:
            t1 = time.clock()
            removed = A.pop(k)
            print(f'N:{n}\tk:{k}\ttime:{time.clock() - t1}')
            A.insert(k, removed) # restore state


N = [100, 1000, 10000, 100000, 1000000]

pop_performance(N)

"""
running times:

N:100           k:0             time:9.6e-06
N:100           k:50            time:2.800000000000014e-06
N:100           k:99            time:2.099999999999997e-06

N:1000          k:0             time:3.500000000000031e-06
N:1000          k:500           time:3.400000000000191e-06
N:1000          k:999           time:2.7000000000000114e-06

N:10000         k:0             time:1.2999999999999123e-05
N:10000         k:5000          time:7.699999999999374e-06
N:10000         k:9999          time:3.299999999997749e-06

N:100000        k:0             time:8.430000000003712e-05
N:100000        k:50000         time:4.2399999999997995e-05
N:100000        k:99999         time:3.000000000030756e-06

N:1000000       k:0             time:0.0009071000000000495
N:1000000       k:500000        time:0.0005267999999998274
N:1000000       k:999999        time:6.300000000347694e-06
"""
