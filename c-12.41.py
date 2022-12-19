"""
Given a sequence S of n elements on which a total order relation is defined,
describe an efficient method for determining whether there are two equal
elements in S. What is the running time of your method?
"""


def has_duplicates(S):
    n = len(S)

    if n > 1:
        array = sorted(S) # O(n*log(n))
        for i in range(1, len(array)): # O(n-1)
            if array[i] == array[i-1]:
                return True
    return False

if __name__ == "__main__":
    S = [9, 11, 2, 40, 9, 44, 2, 4, 6]
    assert has_duplicates(S)

    S = [11]
    assert not has_duplicates(S)

    S = [5, 5]
    assert has_duplicates(S)
