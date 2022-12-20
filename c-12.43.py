"""
Let S be a sequence of n integers. Describe a method for printing out all the pairs of
inversions in S in O(n+k) time, where k is the number of such inversions.
"""


def insertion_sort(S, cnt=0):
    for i in range(1, len(S)):
        j = i - 1
        temp = S[i]

        while S[j] > temp and j >= 0:
            S[j+1] = S[j]
            j -= 1
            cnt += 1

        S[j+1] = temp
    return cnt

if __name__ == "__main__":
    A = [2, 0, 1, 4, 3]
    cnt = insertion_sort(A)
    assert cnt == 3

    A = [2, 1]
    cnt = insertion_sort(A)
    assert cnt == 1

    A = []
    cnt = insertion_sort(A)
    assert cnt == 0


