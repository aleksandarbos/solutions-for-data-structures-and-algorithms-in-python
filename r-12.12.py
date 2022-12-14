"""
If the outermost while loop of our implementation of inplace_quick_sort were changed to
use condition left < right there would be a flaw. Explain the flaw and give a specific input sequence on which such an implementation fails.
"""

def quicksort(S, a, b):
    if a >= b:
        return

    pivot = S[b]
    left = a
    right = b - 1

    while left < right: # <------------- change
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
    S = [100, 100, 100, 100, 1, 100, 100, 100, 100, 100]

    quicksort(S, 0, len(S)-1)
    assert S != sorted(S)
    assert S == [100, 100, 100, 100, 1, 100, 100, 100, 100, 100]
    #    first partition --------^   ^------------------- second partition

    """
    in this case, both left and right will be equal to 4 pointing to "1". when left == right
    (4 == 4) then left won't increase for 1 more, which would leave "1" to be part of the first
    partition (a, left-1), therefore, "1" will end up sorted in 2nd partition which is not
    something we want.
    """
