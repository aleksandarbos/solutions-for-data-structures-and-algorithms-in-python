"""
initial impl of quick-sort algorithm using deque.
"""

from collections import deque

def quicksort(S):
    n = len(S)

    if n < 2:
        return

    p = S.pop()
    l = deque()
    e = deque([p])
    g = deque()


    while len(S) > 0:
        el = S.pop()
        if el < p:
            l.appendleft(el)
        elif el > p:
            g.appendleft(el)
        else:
            e.appendleft(el)

    quicksort(l)
    quicksort(g)

    while len(l) > 0:
        S.append(l.popleft())
    while len(e) > 0:
        S.append(e.popleft())
    while len(g) > 0:
        S.append(g.popleft())

if __name__ == "__main__":
    a = [85, 24, 63, 45, 17, 31, 96, 50, 100]
    quicksort(a)
    assert a == [17, 24, 31, 45, 50, 63, 85, 96, 100]
