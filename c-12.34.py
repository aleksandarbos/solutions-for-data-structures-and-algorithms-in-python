"""
Suppose we are given an n-element sequence of S such as that each element in S represents
a different vote for president, where each vote is given as an integer representing a
candidate, yet the integers may be arbitrarily large (even if the number of candidates is not).
Design an O(n*log(n)) time algorithm to see who wins the election S represents, assuming that
the candidate with the most votes wins.
"""


def group_values(S):
    S.sort()
    result = {}

    for i in range(1, len(S)):
        result.setdefault(S[i], 1)
        if S[i] == S[i-1]:
            result[S[i]] += 1
    return result

if __name__ == "__main__":
    S = [3, 1, 3, 3, 1, 1, 5, 101, 2, 1, 3, 1, 101]

    results = group_values(S)
    max_value = max(results.values())

    top_candidates = [c for c,v in results.items() if v == max_value]

    print(f'the voting results are: {results}')

    if len(top_candidates) > 1:
        print(f'voting is tie between candidates: {top_candidates}')
    else:
        print(f'and the winner is candidate: {top_candidates[0]}')

    """
    the voting results are: {1: 5, 2: 1, 3: 4, 5: 1, 101: 2}
    and the winner is candidate: 1
    """
