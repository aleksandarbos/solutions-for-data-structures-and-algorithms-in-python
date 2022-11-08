"""
For an ideal compression function, the capacity of the bucket array for a hash table should be
a prime number. Therefore, we consider the problem of locating a prime number in a range [M, 2M].
Implement a method for finding such a prime by using the sieve algorithm. In this algorithm, we
allocate a 2M cell Boolean array A, such that cell i i associated with the integer i. We then
initialize the array cells to be all true, and we "mark off" all the cells that are multiples of
2, 3, 5, 7 and so on. This process can stop after it reaches a number larger than sqrt(2M).
"""
def iter_primes(M):
    """
    primes within range [M, 2M]
    time - O(n)
    space - O(n)
    """
    A = [(i, True) for i in range(M, 2*M)]

    for idx, (num, _) in enumerate(A):
        for n in [2, 3, 5, 7]:
            if num != n and num % n == 0:
                A[idx] = (num, False)

    for i in range(0, len(A)):
        if A[i][1]:
            yield A[i][0]


if __name__ == "__main__":
    print(list(iter_primes(60)))
