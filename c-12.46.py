"""
Let A and B be two sequences of n integers each. Given an integer m,
describe an O(n*log(n))-time algorithm for determining if there is an integer a
in A and integer b in B such that m = a + b.
"""


def check_sum(A, B, m):
    h = {}

    for a in A: # O(n)
        h.setdefault(m - a, 1)

    for b in B: # O(n)
        if h.get(b) == 1:
            return True
    return False

if __name__ == "__main__":
    A = [1, 3, 5]
    B = [2, 4, 6]
    m = 7

    result = check_sum(A, B, m)
    assert result == True
