"""
Bob has a set A of n nuts and a set B ogf n bolts, such that each nut in A has a unique matching
bolt in B. Unfortunately, the nuts in A all look the same, and the bolts in B all look the same as well. The only kind of a comparison that Bob can make is to take a nut-bolt pair (a, b, such that a
is in A and b is in B, and test it to see if the threads of a are larger, smaller or a perfect
match with the threads of b. Describe and analyze an efficient algorithm for Bob to match up
all of his nuts and bolts.
"""

def partition(arr, low, high, pivot):
    i = low
    j = low
    while j < high:
        if (arr[j] < pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif (arr[j] == pivot):
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1
        j += 1
    arr[i], arr[high] = arr[high], arr[i]

    return i


def quicksort_inplace(bolts, nuts, lo=0, hi=None):
    if hi <= lo:
        return

    pivot = partition(nuts, lo, hi, bolts[hi])
    partition(bolts, lo, hi, nuts[pivot])

    quicksort_inplace(bolts, nuts, lo, pivot-1)
    quicksort_inplace(bolts, nuts, pivot+1, hi)



if __name__ == "__main__":
    nuts = [2, 6, 8, 7, 1, 5, 3, 4, 9]
    bolts = [6, 2, 7, 5, 9, 4, 3, 1, 8]

    quicksort_inplace(bolts, nuts, 0, len(nuts)-1)
    print(f'{bolts} <- bolts')
    print(f'{nuts} <- nuts')

    assert bolts == nuts
