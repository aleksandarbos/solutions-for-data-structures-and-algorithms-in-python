"""
randomized quick-select
"""

import random

def quickselect(S, kth):
    """
    selects kth smallest element from the unordered sequence S
    """
    if len(S) == 1:
        return S[0]

    L, G, E = [], [], []
    pivot = random.choice(S)

    for i in range(len(S)):
        if S[i] < pivot:
            L.append(S[i])
        elif S[i] > pivot:
            G.append(S[i])
        else:
            E.append(S[i])

    if kth <= len(L):
        return quickselect(L, kth)
    elif kth <= len(L) + len(E):
        return pivot
    else:
        kth -= len(L) + len(E)
        return quickselect(G, kth)

if __name__ == "__main__":
    n = 10
    S = random.sample(range(50), n) # random n distinct numbers, each in between 0-50
    k = random.randint(1, n)

    kth = quickselect(S, k)
    S.sort()
    sorted_k = S.index(kth)
    assert k == sorted_k+1
