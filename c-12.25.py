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
    from time import time

    T = [100000, 1000000, 20000000]
    for t in T:
        t1 = time()
        for i in range(t):
            is_sorted(S)
        print(f'is_sorted for {t} iterations completed in: {time() - t1}')

        t1 = time()
        for i in range(t):
            is_sorted_2(S)
        print(f'is_sorted_2 for {t} iterations completed in: {time() - t1}')

    """
    sequence: [19, 8, 41, 8, 27, 16, 33, 49, 4, 23] is sorted: False
    sequence: [4, 8, 8, 16, 19, 23, 27, 33, 41, 49] is sorted: True
    is_sorted for 100000 iterations completed in: 0.4223442077636719
    is_sorted_2 for 100000 iterations completed in: 0.26900458335876465
    is_sorted for 1000000 iterations completed in: 2.89949369430542
    is_sorted_2 for 1000000 iterations completed in: 2.6019232273101807
    is_sorted for 20000000 iterations completed in: 58.032275676727295
    is_sorted_2 for 20000000 iterations completed in: 62.428250789642334
    """
