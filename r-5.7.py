"""
R-5.7 Let A be an array of size n ≥ 2 containing integers from 1 to n−1, inclusive,
with exactly one repeated. Describe a fast algorithm for finding the integer in A that is repeated."""

import random

def sample(n=2):
    assert n >= 2

    a = [i for i in range(1, n)]
    a.append(random.choice(a))
    random.shuffle(a)
    return a


def find1(l):
    l.sort() # O(nlogn)
    for i in range(1, len(l)):
        if l[i] == l[i-1]:
            return l[i]
    return None


def find2(l):
    """

    len(l) = 10
    timeit 100000 loops, best of 3: 12.9 us per loop
    len(l) = 1000
    100000 loops, best of 3: 10.4 us per loop
    """
    n = len(l) # O(1)
    return sum(l) - (n*n - n) / 2 # O(n) for sum()

s = sample(10)
print(s)
print(find1(s))
print(find2(s))
