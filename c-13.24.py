"""
Say that a pattern P of length m is a circular substring of a text T of length
n > m if P is a (normal) substring of T, or if P is equal to the concatenation
of a suffix of T and a prefix of T, that is, if there is an index 0 ≤ k < m,
such that P = T[n-m+k :n]+T [0:k]. Give an O(n+m)-time algorithm
for determining whether P is a circular substring of T.
"""


def kmp_find(T, P):
    n, m = len(T), len(P)
    if m == 0: return -1

    fail = compute_kmp_fail(P)

    j = 0
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

def is_circular_substring(T, P):
    T_prim = T * 2 # T' = T + T, which "normalizes" circularity, so it can be searched upon
    return kmp_find(T_prim, P) # like any ordinary string

if __name__ == "__main__":
    T = "abcd"
    P = "dab"

    assert is_circular_substring(T, P) != -1
