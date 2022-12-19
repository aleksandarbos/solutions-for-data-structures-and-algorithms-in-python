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
    S = [0] * n

    print(f'testing for array S: {S}')

    from shared import benchmark

    ranges = [10, 100, 100000]
    benchmark(quicksort, iter_nums=ranges, S=S)
    benchmark(merge_sort, iter_nums=ranges, seq=S)

    """
    testing for array S: [1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1]
    running quicksort for 10 iterations, time elapsed: 0.0009996891021728516
    running quicksort for 100 iterations, time elapsed: 0.010211467742919922
    running quicksort for 100000 iterations, time elapsed: 9.153722047805786
    running merge_sort for 10 iterations, time elapsed: 0.007335186004638672
    running merge_sort for 100 iterations, time elapsed: 0.024003982543945312
    running merge_sort for 100000 iterations, time elapsed: 27.144846200942993


    testing for array S: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    running quicksort for 10 iterations, time elapsed: 0.0
    running quicksort for 100 iterations, time elapsed: 0.0038824081420898438
    running quicksort for 100000 iterations, time elapsed: 7.408846616744995
    running merge_sort for 10 iterations, time elapsed: 0.015739917755126953
    running merge_sort for 100 iterations, time elapsed: 0.023989200592041016
    running merge_sort for 100000 iterations, time elapsed: 20.2160484790802

    """
