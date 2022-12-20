"""
Let S be a sequence of n elements on which a total order relation is defined. Recall that
inversion in S is a pair of elements x and y such that x appears before y in S, but x > y.
Describe an algorithm running in O(n*log(n)) time for determining the number of inversions in S.
"""

def merge(A, B, S, cnt=0):
    cnt_a, cnt_b = 0, 0

    while cnt_a + cnt_b < len(A) + len(B):
        if cnt_b >= len(B) or cnt_a < len(A) and A[cnt_a] < B[cnt_b]:
            S[cnt_a + cnt_b] = A[cnt_a]
            cnt_a += 1
        else:
            if cnt_a < len(A) and B[cnt_b] < A[cnt_a]:
                cnt += 1 # append inversion occurrence to cnt list instance
            S[cnt_a + cnt_b] = B[cnt_b]
            cnt_b += 1
    return cnt

def merge_sort(S):
    cnt = 0
    n = len(S)

    if n < 2:
        return cnt

    mid = n // 2
    s1 = S[:mid]
    s2 = S[mid:]

    cnt += merge_sort(s1)
    cnt += merge_sort(s2)

    cnt += merge(s1, s2, S)
    return cnt


if __name__ == "__main__":
    S = [3, 45, 1, 2, 0, 44]
    cnt = merge_sort(S)
    assert cnt == 6

    S = [1, 20, 6, 4, 5]
    cnt = merge_sort(S)
    assert cnt == 5

    S = [1, 2]
    cnt = merge_sort(S)
    assert cnt == 0

    S = []
    cnt = merge_sort(S)
    assert cnt == 0


