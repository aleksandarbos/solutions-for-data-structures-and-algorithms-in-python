"""
Redo Exercise C-13.19, adapting the Knuth-Morris-Pratt pattern-matching
algorithm appropriately to implement a function count kmp(T,P).
"""

def find_kmp(T, P, start=0):
    n, m = len(T), len(P)
    if m == 0 or start > n - m: return -1

    fail = compute_kmp_fail(P)

    j = 0 + start
    k = 0

    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return -1

def compute_kmp_fail(P):
    m = len(P)
    fail = [0] * m
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail

def count_kmp(T, P):
    n, m = len(T), len(P)
    if m == 0: return n + 1
    k = 0
    cnt = 0
    while True:
        j = find_kmp(T, P, start=k)
        if j == -1:
            break
        else:
            cnt += 1
            k = j + m
    return cnt


if __name__ == "__main__":
    T = 'test to last'
    P = 'st'
    assert count_kmp(T, P) == T.count(P)
    assert find_kmp(T, P, start=len(T)-1) == -1 # len(T) - start < len(P) - can't be there

    T = 'test'
    P = ''
    assert count_kmp(T, P) == T.count(P)
