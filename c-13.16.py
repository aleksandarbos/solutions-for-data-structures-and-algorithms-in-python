"""
Adapt the brute-force pattern-matching algorithm in order to implement a function
rfind_brute(T, P), that returns the index at which the rightmost occurrence of pattern P
within the text T, if any.
"""

def find_brute(T, P):
    n, m = len(T), len(P)
    for i in range(n-m+1):
        k = 0
        while k < m and T[i + k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1

def rfind_brute(T, P):
    n, m = len(T), len(P)
    for i in range(n, m-1, -1):
        k = 0
        while k < m and T[i-m + k] == P[k]:
            k += 1
        if k == m:
            return i-m
    return -1


if __name__ == "__main__":
    T = 'ababaaa'
    P = 'ba'

    assert find_brute(T, P) == 1
    assert rfind_brute(T, P) == 3

    T = ''
    P = 'a'

    assert find_brute(T, P) == -1
    assert rfind_brute(T, P) == -1

