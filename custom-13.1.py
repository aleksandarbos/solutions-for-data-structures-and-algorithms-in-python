"""
brute-force impl of the pattern search within the text
"""

def find(T, P):
    """
    returns 1 if P is present within text T, else -1
    """
    n = len(T)
    m = len(P)

    for i in range(n-m+1):
        j = 0
        while j < m and T[i+j] == P[j]:
            if j == m-1:
                return i
            else:
                j += 1
    return -1

def find_brute(T, P):
    n, m = len(T), len(P)
    for i in range(n-m+1):
        k = 0
        while k < m and T[i + k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1

if __name__ == "__main__":
    T = "abcbacbcbacabcabccbaccbacbcb"
    P = "bcabc"

    assert find(T, P) == T.find(P, 1) == find_brute(T, P)
