"""
The count method of Python's str class reports the maximum number of non-overlapping occurrences of
a pattern within a string. For example, the call 'abababa'.count('aba') results with 2 (not 3). Adapt
the brute-force pattern-matching algorithm to implement a function, count_brute(T, P) with similar outcome.
"""

def find_brute(T, P, start=0):
    n, m = len(T), len(P)
    if start > n - 1 or start > n - m:
        return -1
    for i in range(start, n-m+1):
        k = 0
        while k < m and T[i + k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1

def count_brute(T, P):
    n, m = len(T), len(P)
    if m == 0: return n + 1
    k = 0
    cnt = 0
    while True:
        j = find_brute(T, P, start=k)
        if j == -1:
            break
        else:
            cnt += 1
            k = j + m
    return cnt

if __name__ == "__main__":
    T = 'alaabababasada'
    P = 'aba'
    assert count_brute(T, P) == T.count(P)

    T = "asdasd"
    P = ""
    assert count_brute(T, P) == T.count(P)
