"""
Suppose that each row of an n x n array A consists of 1's and 0's such that,
in any row of A, all the 1's come before any 0's in that row. Assuming A
is already in the memory, describe a method running in O(nlogn) time (not in O(n^2) time!) for
counting the number of 1's in A.
"""

def bin_search(seq, k, low=0, high=None):
    """
    finds rightmost index of searched value less than or equal to key k.
    runs in O(logn).
    """
    if high is None:
        high = len(seq)-1

    if high < low:
        return high + 1
    else:
        mid = (high + low) // 2
        if seq[mid] > k:    # opposite sign (bc arrays are max oriented sort - ones go first)
            return bin_search(seq, k, mid+1, high)
        else:
            return bin_search(seq, k, low, mid-1)

def count_ones(A):
    """
    method that counts number of ones in the matrix.
    time complexity: O(nlogn)
    """
    total = 0

    for i in range(len(A)):       # n times
        inc = bin_search(A[i], 0) # O(logn)
        if inc > len(A[i]):       # O(1) for all operations bellow
            inc = len(A[i])
        elif inc < 0:
            inc = 0
        total += inc

    return total

if __name__ == "__main__":
    import random

    n = 5 # matrix dimension
    A = []

    for i in range(0, n):
        num_of_ones = random.randint(0, n)
        A.append([1] * num_of_ones)
        if num_of_ones < n:
            A[-1] += [0] * (n - num_of_ones)

    print(f'counting number of 1\'s in matrix A:')
    print(A)
    print(f'number of 1\'s in matrix A is: {count_ones(A)}')
