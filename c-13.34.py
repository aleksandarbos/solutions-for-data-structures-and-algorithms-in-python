"""
Describe an efficient algorithm to find the longest palindrome that is a
suffix of a string T of length n. Recall that a palindrome is a string that is
equal to its reversal. What is the running time of your method?
"""

def longest_palindrome_in_suffix_of(T):
    left, right = 0, len(T)-1
    max_palindrome = 0

    while left < right:
        if T[left] == T[right]:
            left += 1
            right -= 1
        else:
            left += 1
            right = len(T)-1
            max_palindrome = left
    return T[max_palindrome:]

if __name__ == "__main__":
    T = "banana"
    assert longest_palindrome_in_suffix_of(T) == "anana"

    T = "anavolimilovana"
    assert longest_palindrome_in_suffix_of(T) == "anavolimilovana"

    T = ""
    assert longest_palindrome_in_suffix_of(T) == ""
