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
    """
    A = [True] * 2*M
    p = 2

    while p*p < 2*M: # is the same as p < sqrt(2*M) (no math module import needed)
        if A[p] is True:
            for i in range(p*p, 2*M, p):
                A[i] = False
        p += 1

    for i in range(len(A)):
        if A[i] and i > M:
            yield i


if __name__ == "__main__":
    M = 60
    expected_primes = [61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    actual_primes = list(iter_primes(M))
    assert actual_primes == expected_primes
