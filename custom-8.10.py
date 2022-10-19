"""
recursive palindrome finder for sentence "s"
"""

def palindrome(s, start=0, stop=None):
    if stop is None:
        stop = len(s) - 1
    if s[start] != s[stop]:
        return False
    elif start < stop:
        return palindrome(s, start + 1, stop - 1)
    return True

def palindrome2(s):
    if len(s) > 0:
        if s[0] != s[-1]:
            return False
        else:
            return palindrome2(s[1:-1])
    return True

def palindrome3(s):
    if len(s) > 0:
        return False if s[0] != s[-1] else palindrome3(s[1:-1]) # one liner if-else
    return True



p1 = "anavolimilovana"
p2 = "test2fest"
p3 = "oko2oko"
print(f"test palindrome: {p1}, result: {palindrome(p1)}")
print(f"test palindrome: {p2}, result: {palindrome(p2)}")
print(f"test palindrome: {p3}, result: {palindrome(p3)}")

