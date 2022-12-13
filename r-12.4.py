"""
Is our array-based implementation of merge-sort given in Section 12.2.2 stable?
Explain why or why not.
"""

from shared_9_chapter import Item

def merge(A, B, S):
    cnt_a, cnt_b = 0, 0

    while cnt_a + cnt_b < len(S):
        if cnt_b == len(B) or (cnt_a < len(A) and A[cnt_a] <= B[cnt_b]):
            S[cnt_a+cnt_b] = A[cnt_a]
            cnt_a += 1
        else:
            S[cnt_a+cnt_b] = B[cnt_b]
            cnt_b += 1

def merge_sort(S):
    n = len(S)

    if n < 2:
        return

    mid = n // 2
    s1 = S[:mid]
    s2 = S[mid:]

    merge_sort(s1)
    merge_sort(s2)

    return merge(s1, s2, S)

if __name__ == "__main__":
    S = [Item(1, 1), Item(0, 1), Item(5, 3), Item(5, 1), Item(2, 1), Item(5, 2),]

    a1 = [4, 7, 9]
    a2 = [1, 5, 8]
    s1 = [0] * (len(a1) + len(a2))
    merge(a1, a2, s1)
    assert s1 == [1, 4, 5, 7, 8, 9]

    merge_sort(S)
    assert S == [Item(0, 1), Item(1, 1), Item(2, 1), Item(5, 3), Item(5, 1), Item(5, 2)]

"""
Yes it's stable. It's preserving the order of the keys with the same value. Merge sort is preserving left-right the position of the key through the recursion tree. See https://qph.cf2.quoracdn.net/main-qimg-9201580b5463a5fed51c02c88e980803 for "1".
"""
