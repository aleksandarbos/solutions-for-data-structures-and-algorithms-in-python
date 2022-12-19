"""
Modify our in-place quick-sort implementation of Code Fragment 12.6 to be a randomized version
of the algorithm as discussed in the Section 12.3.1.
"""
import random

def quicksort(S, a=0, b=None):
    if b is None:
        b = len(S) - 1

    if a >= b:
        return

    rand = random.randint(a, b) # <--- random pivoting
    pivot = S[rand]
    S[rand], S[b] = S[b], S[rand] # put pivot at the end of the list

    left = a
    right = b - 1

    while left <= right:
        while left <= right and S[left] < pivot:
            left += 1

        while left <= right and S[right] > pivot:
            right -= 1

        if left <= right:
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right -1

    S[left], S[b] = S[b], S[left] # replace pivot with left position when done
    quicksort(S, a, left-1)
    quicksort(S, left+1, b)

if __name__ == "__main__":
    n = 10
    S = [random.randint(0, 50) for _ in range(n)]

    quicksort(S)
    assert S == sorted(S)
