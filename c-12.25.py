"""
Linda claims to have an algorithm that takes an input sequence S and produces
an output sequence T that is a sorting of the n elements in S.
  a. Give an algorithm, is_sorted, that tests in O(n) time if T is sorted.
  b. Explain why the algorithm is_sorted is not sufficient to prove a particular output T to
  Linda's algorithm is a sorting of S.
  c. Describe what additional information Linda's algorithm could output so that her
  algorithm's correctness could be established on any given S and T in O(n) time.
"""

import random

# a.
def is_sorted(S, key=lambda x: x):
    for i in range(len(S) - 1):
        if key(S[i + 1]) < key(S[i]):
            return False
    return True

def is_sorted_2(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]): # i is the index of the previous element
            return False
    return True

if __name__ == "__main__":
    n = 10
    S = [random.randint(0, 50) for _ in range(n)]

    print(f'sequence: {S} is sorted: {is_sorted(S)}')

    S.sort()
    print(f'sequence: {S} is sorted: {is_sorted(S)}')

    """
    b. we don't know if T contains all the elements of the S
    c.
    """

    from shared import benchmark
    T = [100000, 1000000, 2000000]
    benchmark(is_sorted, T, S=S)
    benchmark(is_sorted_2, T, lst=S)

    """
    running is_sorted for 100000 iterations, time elapsed: 1.8002853393554688
    running is_sorted for 1000000 iterations, time elapsed: 24.147040843963623
    running is_sorted for 2000000 iterations, time elapsed: 49.521862506866455
    running is_sorted_2 for 100000 iterations, time elapsed: 2.14522123336792
    running is_sorted_2 for 1000000 iterations, time elapsed: 21.585848569869995
    running is_sorted_2 for 2000000 iterations, time elapsed: 43.973034381866455
    """
