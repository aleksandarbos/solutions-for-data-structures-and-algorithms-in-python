"""
Describe and analyze an efficient method for removing all duplicates from a collection A of n elements.
"""


def remove_duplicates(S):
    S.sort() # O(n*log(n))
    j = 0

    while j < len(S)-1: # O(n-1)
        if S[j + 1] == S[j]:
            del S[j]
        else:
            j += 1


def remove_duplicates_optimized(S):
    S.sort() # O(n*log(n))
    j = len(S) - 1

    while j > 0: # O(n-1)
        if S[j - 1] == S[j]:
            del S[j]
        j -= 1

if __name__ == "__main__":
    S = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 1, 2, 3, 3, 3, 2, 1]
    S1 = S[:]
    S2 = S[:]
    remove_duplicates(S1)
    remove_duplicates_optimized(S2)

    assert S1 == [1, 2, 3]
    assert S2 == [1, 2, 3]

    from shared import benchmark

    benchmark(remove_duplicates_optimized, S=S[:])
    benchmark(remove_duplicates, S=S[:])
    """
    running remove_duplicates_optimized for 1000 iterations, time elapsed: 0.07072329521179199
    running remove_duplicates_optimized for 100000 iterations, time elapsed: 3.829793691635132
    running remove_duplicates_optimized for 1000000 iterations, time elapsed: 29.791290521621704
    running remove_duplicates for 1000 iterations, time elapsed: 0.03816819190979004
    running remove_duplicates for 100000 iterations, time elapsed: 3.3108885288238525
    running remove_duplicates for 1000000 iterations, time elapsed: 33.735276222229004
    """
