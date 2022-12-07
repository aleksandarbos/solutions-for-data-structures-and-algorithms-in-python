"""
going through some simple basic sorting algorithms which run in O(n^2) time.
"""

def bubble_sort(seq):
    for _ in range(len(seq)):
        for j in range(1, len(seq)):
            if seq[j] < seq[j-1]:
                seq[j-1], seq[j] = seq[j], seq[j-1]
    return seq

def selection_sort(seq):
    for i in range(len(seq)):
        min_idx = i
        for j in range(i, len(seq)):
            if seq[j] < seq[min_idx]:
                min_idx = j
        seq[i], seq[min_idx] = seq[min_idx], seq[i]
    return seq

def insertion_sort(seq):
    for i in range(len(seq)-1):
        j = i + 1
        while j > 0 and seq[j] < seq[j-1]:
            seq[j], seq[j-1] = seq[j-1], seq[j]
            j -= 1
    return seq


if __name__ == "__main__":
    a = [4, -6, 11, 9, 22, 105, -224, 0, 113, 5, 132, 7, 94, 41]

    # passing array copy bc of mutable operations
    assert bubble_sort(a[:]) == sorted(a)
    assert selection_sort(a[:]) == sorted(a)
    assert insertion_sort(a[:]) == sorted(a)
