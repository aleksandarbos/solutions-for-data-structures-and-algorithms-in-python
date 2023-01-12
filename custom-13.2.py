"""
boyer-moore pattern search impl
"""

def find_boyer_moore(T, P):
    n, m = len(T), len(P)
    if m == 0: return -1

    last = {}
    for i in range(m):
        last[P[i]] = i

    i = m-1
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

if __name__ == "__main__":
    T = 'dva su veoma losa ubila milosa naseg'
    P = 'losa'

    assert find_boyer_moore(T, P) == T.find(P)
