"""
right to left boyer-moore pattern search impl
"""

def rfind_boyer_moore(T, P):
    n, m = len(T), len(P)
    if m == 0: return -1

    last = {}
    for idx, c in enumerate(reversed(P)): # symmetric last
        last[c] = idx

    i = n - m
    k = 0

    while i > 0:
        if T[i] == P[k]:
            if k == m - 1:
                return i - m + 1
            else:
                k += 1
                i += 1
        else:
            j = last.get(T[i], -1)
            if j > k:
                i -= m - (j + 1)
            else:
                i -= 1
            k = 0
    return -1

if __name__ == "__main__":
    T = 'dva su veoma losa ubila milosa naseg'
    P = 'losa'

    assert rfind_boyer_moore(T, P) == T.rfind(P)
