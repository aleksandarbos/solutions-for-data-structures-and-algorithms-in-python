"""
An algorithm that sorts key-value entries by key is said to be straggling if,
any time two entries e-i and e-j have equal keys, but e-i appears before e-j
in the input, and the algorithm places e-i after e-j in the output. Describe a change to the
merge sort algorithm in Section 12.2 to make it straggling.
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

    return merge(s2, s1, S) # <------ the change (this will undo left-right order)

if __name__ == "__main__":
    S = [Item(1, 1), Item(0, 1), Item(5, 3), Item(5, 1), Item(2, 1), Item(5, 2),]

    merge_sort(S)

    # expect different results
    assert S != [Item(0, 1), Item(1, 1), Item(2, 1), Item(5, 3), Item(5, 1), Item(5, 2)]
