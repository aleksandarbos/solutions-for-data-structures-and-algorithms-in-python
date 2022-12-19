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

    n = 10
    S = [round(random.random()) for _ in range(n)]

    print(f'testing for array S: {S}')

    from shared import benchmark

    ranges = [100000, 1000000, 2000000]
    benchmark(insertion_sort, iter_nums=ranges, S=S)
    benchmark(bin_sort, iter_nums=ranges, S=S)

    """
    testing for array S: [0, 1, 0, 0, 1, 1, 1, 1, 1, 1]
    running insertion_sort for 100000 iterations, time elapsed: 1.8521027565002441
    running insertion_sort for 1000000 iterations, time elapsed: 19.888442516326904
    running insertion_sort for 2000000 iterations, time elapsed: 38.425713539123535
    running bin_sort for 100000 iterations, time elapsed: 1.8709335327148438
    running bin_sort for 1000000 iterations, time elapsed: 17.90862202644348
    running bin_sort for 2000000 iterations, time elapsed: 34.60061478614807
    """
