"""
Redo the previous problem (C-13.20), adapting the Boyer-Moore pattern-matching
algorithm in order to implement a function count boyer moore(T,P).
"""


def find_boyer_moore(T, P, start=0):
    n, m = len(T), len(P)
    if m == 0:
        return n + 1
    elif start > n - m:
        return -1

    last = {}
    for i in range(m):
        last[P[i]] = i

    i = start + m-1
    k = m-1

    while i < n:
        if T[i] == P[k]:
            if k == 0:
                return i
            else:
                k -= 1
                i -= 1
        else:
            j = last.get(T[i], -1)
            if j < k:
                i += m - (j + 1)
            else:
                i += 1
            k = m - 1
    return -1

def count_boyer_moore(T, P):
    n, m = len(T), len(P)
    if m == 0: return n + 1
    k = 0
    cnt = 0
    while True:
        j = find_boyer_moore(T, P, start=k)
        if j == -1:
            break
        else:
            cnt += 1
            k = j + m
    return cnt

if __name__ == "__main__":
    T = 'test to last'
    P = 'st'
    assert count_boyer_moore(T, P) == T.count(P)

    T = 'test'
    P = ''
    assert count_boyer_moore(T, P) == T.count(P)
