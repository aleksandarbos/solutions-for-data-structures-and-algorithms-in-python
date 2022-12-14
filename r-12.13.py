"""
If the outermost while loop of our implementation of inplace_quick_sort were changed to
use condition left < right there would be a flaw. Explain the flaw and give a specific input sequence on which such an implementation fails. (inner if statement within the greater while loop)
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

        if left < right: # <------------- change
            S[left], S[right] = S[right], S[left]
            left, right = left + 1, right -1

    S[left], S[b] = S[b], S[left] # replace pivot with left position when done
    quicksort(S, a, left-1)
    quicksort(S, left+1, b)

if __name__ == "__main__":
    S = [2, 2, 2, 2]

#    quicksort(S, 0, len(S)-1)

    """
    the problem occurs when both left and right are equal, and elements in the array are
    equal to the pivot, therefore, there isn't anything that can either update left nor right,
    and making the algorithm stuck in the greater "while left <= right" loop.
    """
