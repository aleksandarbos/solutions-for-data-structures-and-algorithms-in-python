"""
Consider a modification of the deterministic version of the quick-sort algorithm where
we choose the element at index n // 2 as our pivot. Describe the kind of sequence that would
cause this version of quick-sort to run in theta(O^n) time.
"""

"""
initial impl of quick-sort algorithm using deque.
"""

from collections import deque

def quicksort(S):
    quicksort.cnt += 1

    n = len(S)

    if n < 2:
        return

    p = S[n//2] # <----- pivot is median
    # p = S.pop()
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
    s = [10,30,50,70,90,100,80,60,40,20]
    # n + n-1 + n-2 + .. 2 = (n*(n-1))/2 = O(n^2)

    quicksort.cnt = 0
    print(f's: {s}')
    quicksort(s)
    print(f'num of times "quicksort" is called: {quicksort.cnt}')

