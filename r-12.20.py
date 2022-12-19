"""
Suppose S is a sequence of n values, each equal to 0 or 1. How long will it take to sort S stably with the bucket-sort algorithm?
"""

from shared_12_chapter import bucketsort

if __name__ == "__main__":
    """
    benchmarking merge-sort vs quicksort for arrays which consists only of 1's and 0's
    """

    import random

    n = 50
    S = [round(random.random()) for _ in range(n)]

    print(f'testing for array S: {S}')

    from shared import benchmark

    ranges = [10, 100, 100000]
    benchmark(bucketsort, iter_nums=ranges, S=S)

    """
    testing for array S: [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0]
    running bucketsort for 10 iterations, time elapsed: 0.0009987354278564453
    running bucketsort for 100 iterations, time elapsed: 0.013993501663208008
    running bucketsort for 100000 iterations, time elapsed: 11.006261587142944
    """
