"""
Give an efficient algorithm for determining if a pattern P is a subsequence
(not substring) of a text T. What is the running time of your algorithm?
"""

def is_subsequence(T, P): # O(n+m)
    n, m = len(T), len(P)
    i, j = 0, 0

    while i < n and j < m:
        if T[i] == P[j]:
            i += 1
            j += 1
        else:
            i += 1
    return j == m


if __name__ == "__main__":
    T = "this is an example text of this test"
    P = "hexle ex of tt"
    assert is_subsequence(T, P)

    T = "this is an example text of this test"
    P = "b"
    assert not is_subsequence(T, P)

    T = "this is an example text of this test"
    P = ""
    assert is_subsequence(T, P)

    T = "Simpl Test Subseq"
    P = "STS"
    assert is_subsequence(T, P)

    T = "Simpl Test Subseq"
    P = "STSS"
    assert not is_subsequence(T, P)
