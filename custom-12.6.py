"""
in-place quicksort implementation using hoare's partition scheme.
"""


def quicksort(S, a, b):
    if a >= b:
        return

    pivot = S[b]
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
    S = [51, -4, 11, 23, 0, -4, 9, 12, 1, 3, 3]

    quicksort(S, 0, len(S)-1)
    assert S == sorted(S)
