"""
Let T be a text of length n, and let P be a pattern of length m. Describe an
O(n+m)-time method for finding the longest prefix of P that is a substring
of T.
"""

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

def longest_prefix_kmp(T, P):
    max_prefix_len = 0
    max_prefix_id = 0

    prefix_len = 0

    n, m = len(T), len(P)
    if m == 0: return -1

    fail = compute_kmp_fail(P)

    j = 0
    k = 0

    while j < n:
        if T[j] == P[k]:
            j += 1
            k += 1
            prefix_len += 1

            if prefix_len > max_prefix_len:
                max_prefix_len = prefix_len
                max_prefix_id = j - prefix_len
        else:
            if k > 0:
                k = fail[k-1]
            else:
                j += 1
            prefix_len = 0

    return max_prefix_id, T[max_prefix_id:max_prefix_id+max_prefix_len]

if __name__ == "__main__":
    T = "aaaab abbbaaa bbbabaaaabb bababa"
    P = "aaaabba"

    assert longest_prefix_kmp(T, P) == (19, 'aaaabb')
