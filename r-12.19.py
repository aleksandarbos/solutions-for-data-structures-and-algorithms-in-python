"""
Suppose S is a sequence of n values, each equal to 0 or 1. How long will it take to sort S
with merge-sort algorithm? What about quick-sort?
"""

from shared_12_chapter import quicksort, merge_sort

if __name__ == "__main__":
    """
    benchmarking merge-sort vs quicksort for arrays which consists only of 1's and 0's
    """

    import random
    from time import time

    n = 50
    S = [round(random.random()) for _ in range(n)]
    # S = [0] * n

    print(f'testing for array S: {S}')

    ranges = [10, 100, 100000]

    for r in ranges:
        print(f'quicksort {r} iterations', end='')
        t1 = time()
        for _ in range(r):
            quicksort(S)
        print(f', time: {time() - t1}')

        print(f'merge-sort {r} iterations', end='')
        t1 = time()
        for _ in range(r):
            merge_sort(S)
        print(f', time: {time() - t1}')

"""
testing for array S: [0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
quicksort for range: 10, time: 0.000997304916381836
merge-sort 10 iterations, time: 0.0030007362365722656
quicksort for range: 100, time: 0.0060138702392578125
merge-sort 100 iterations, time: 0.02498650550842285
quicksort for range: 100000, time: 3.9110195636749268
merge-sort 100000 iterations, time: 16.3315110206604


testing for array S: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
quicksort for range: 10, time: 0.0010004043579101562
merge-sort 10 iterations, time: 0.002999544143676758
quicksort for range: 100, time: 0.010994672775268555
merge-sort 100 iterations, time: 0.0219876766204834
quicksort for range: 100000, time: 2.9180185794830322
merge-sort 100000 iterations, time: 14.838016748428345

"""
