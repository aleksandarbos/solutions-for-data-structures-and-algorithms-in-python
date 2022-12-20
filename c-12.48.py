"""
Our quick-select implementation can be made more space-efficient by initially computing
only the counts for sets L, E, and G, creating only the new subset that will be needed
for recursion. Implement such a version.
"""

import random

def quick_select(S, kth):
    n = len(S)

    if n < 2:
        return S[0]

    pivot = random.choice(S)
    l, g, e = 0, 0, 0

    for el in S:
        if el < pivot:
            l += 1
        elif el > pivot:
            g += 1
        else:
            e += 1

    if kth <= l:
        L = [el for el in S if el < pivot]
        return quick_select(L, kth)
    elif kth <= l + e:
        return pivot
    else:
        G = [el for el in S if el > pivot]
        kth -= l + e
        return quick_select(G, kth)

if __name__ == "__main__":
    S = [3, 6, 1, 2, 4, 6, 7]
    kth = 5
    assert quick_select(S, kth) == 6

    S = [7, 7, 7]
    kth = 3
    assert quick_select(S, kth) == 7

    S = [0]
    kth = 1
    assert quick_select(S, kth) == 0
