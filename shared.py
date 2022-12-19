from time import time
from copy import deepcopy

def benchmark(handler, iter_nums=[1000, 100000, 1000000], *args, **kwargs):
    for iter_n in iter_nums:
        t = time()
        for _ in range(iter_n):
            handler(*deepcopy(args), **deepcopy(kwargs)) # deepcopy to annulate mutable operations
        print(f'running {handler.__name__} for {iter_n} iterations, time elapsed: {time() - t}')
