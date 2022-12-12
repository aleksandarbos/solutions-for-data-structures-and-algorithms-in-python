"""
quicksort-in place implementation with lomuto partitions.
"""

def lomuto_partition(S, low=0, high=None):
    high = high or len(S)-1
    pivot = S[high]
    i = low - 1

    for j in range(low, high):
        if S[j] <= pivot:
            i += 1
            S[j], S[i] = S[i], S[j]
    S[i+1], S[high] = S[high], S[i+1]
    return i + 1

def quicksort_inplace(S, lo=0, hi=None):
    n = len(S)
    hi = hi if hi is not None else n-1

    if hi <= lo:
        return

    i = lomuto_partition(S, lo, hi)
    quicksort_inplace(S, lo, i-1)
    quicksort_inplace(S, i+1, hi)


if __name__ == "__main__":
    a = [5, 0, 1, 9, 2]
    b = a[:]
    idx = lomuto_partition(a, 0, len(a)-1)
    assert a == [0, 1, 2, 9, 5]
    assert idx == 2

    quicksort_inplace(b)
    assert b == sorted(b)
