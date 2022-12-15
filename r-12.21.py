"""
Given a sequence S of n values, each equal to 0 or 1, describe an in-place method for
sorting S.
"""

from shared_12_chapter import insertion_sort

def bin_sort(S):
    zeros_cnt = 0
    for i in range(len(S)):
        if S[i] == 0:
            zeros_cnt += 1
    for i in range(len(S)):
        if i < zeros_cnt:
            S[i] = 0
        else:
            S[i] = 1

if __name__ == "__main__":
    import random
    from time import time

    n = 10
    S = [round(random.random()) for _ in range(n)]

    print(f'testing for array S: {S}')

    ranges = [100000, 1000000, 20000000]

    for r in ranges:
        print(f'insertion_sort {r} iterations', end='')
        t1 = time()
        for _ in range(r):
            insertion_sort(S)
        print(f', time: {time() - t1}')

        print(f'bin_sort {r} iterations', end='')
        t1 = time()
        for _ in range(r):
            bin_sort(S)
        print(f', time: {time() - t1}')

"""
testing for array S: [0, 1, 0, 1, 1, 1, 1, 0, 0, 1]
insertion_sort 100000 iterations, time: 0.4297511577606201
bin_sort 100000 iterations, time: 0.4107651710510254
insertion_sort 1000000 iterations, time: 2.793397903442383
bin_sort 1000000 iterations, time: 2.6274960041046143
insertion_sort 20000000 iterations, time: 62.46323275566101
bin_sort 20000000 iterations, time: 54.04670000076294
"""
