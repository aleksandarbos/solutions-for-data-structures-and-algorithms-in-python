"""
exercise for using stack to find a matching parentheses
"""


def is_valid(expression):
    lefts = '{[('
    rights = '}])'
    s = []

    for c in expression:
        if c in lefts:
            s.append(c)
        elif c in rights:
            if len(s) == 0:
                return False
            if rights.index(c) != lefts.index(s.pop()):
                return False
    return len(s) == 0

e1 = "[()]"
e2 = "{[{()}]}"
e3 = "}"
e4 = "{{()}"

print(is_valid(e1))
print(is_valid(e2))
print(is_valid(e3))
print(is_valid(e4))
