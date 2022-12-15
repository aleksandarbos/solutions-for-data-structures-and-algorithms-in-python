"""
Suppose S is a sequence of n values, each equal to 0 or 1. How long will it take to sort S stably with the bucket-sort algorithm?
"""

from shared_12_chapter import bucketsort

if __name__ == "__main__":
    """
    benchmarking merge-sort vs quicksort for arrays which consists only of 1's and 0's
    """

    import random
    from time import time

    n = 50
    S = [round(random.random()) for _ in range(n)]

    print(f'testing for array S: {S}')

    ranges = [10, 100, 100000]

    for r in ranges:
        print(f'bucket-sort {r} iterations', end='')
        t1 = time()
        for _ in range(r):
            bucketsort(S)
        print(f', time: {time() - t1}')

"""
testing for array S: [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1]
bucket-sort 10 iterations, time: 0.0009987354278564453
bucket-sort 100 iterations, time: 0.013002634048461914
bucket-sort 100000 iterations, time: 8.734952688217163
"""
