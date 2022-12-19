"""
Consider the voting problem from Exercise C-12.34, but now suppose that integers 1 to k are used
to identify k < n candidates. Describe an O(n) time algorithm to determine who wins the election.
"""

def group_values(S): # O(n)
    result = {}

    for val in S:
        result.setdefault(val, 0)
        result[val] += 1

    return result

if __name__ == "__main__":

    # k = 3 candidates
    S = [1, 3, 1, 2, 2, 1, 3, 3, 1, 2, 2, 3, 2]
    result = group_values(S)

    winner = max(result, key=lambda key: result.get(key)) # O(n)
    print(f'winner is: {winner}') # total time complexity: 2 * O(n)
