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


if __name__ == "__main__":
    e1 = "[()]"
    e2 = "{[{()}]}"
    e3 = "}"
    e4 = "{{()}"

    assert is_valid(e1)
    assert is_valid(e2)
    assert not is_valid(e3)
    assert not is_valid(e4)
