"""
mutable implementation of merge-sort algorithm.
"""

def merge(S1, S2, S):
    """
    mutable impl of merging two sorted arrays S1 and S2 into sequence S.
    """
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or i < len(S1) and S1[i] < S2[j]:
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1

def merge_sort(seq):
    """
    mutable implementation of merge-sort algorithm
    """
    n = len(seq)

    if n < 2:
        return

    mid = n // 2
    s1 = seq[:mid]
    s2 = seq[mid:]

    merge_sort(s1)
    merge_sort(s2)

    merge(s1, s2, seq)

if __name__ == "__main__":
    A = [3, 7]
    B = [2, 5]
    result = [None] * (len(A) + len(B))
    merge(A, B, result)
    assert result == [2, 3, 5, 7]

    a = [85, 24, 63, 45, 17, 31, 96, 50, 100]
    merge_sort(a)
    assert a == [17, 24, 31, 45, 50, 63, 85, 96, 100]
