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

def merge(S1, S2, S):
    """
    mutable impl of merging two sorted arrays S1 and S2 into sequence S.
    """
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or i < len(S1) and S1[i] < S2[j]:
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1

def merge_sort(seq):
    """
    mutable implementation of merge-sort algorithm
    """
    n = len(seq)

    if n < 2:
        return

    mid = n // 2
    s1 = seq[:mid]
    s2 = seq[mid:]

    merge_sort(s1)
    merge_sort(s2)

    merge(s1, s2, seq)

def insertion_sort(S):
    for i in range(1, len(S)):
        j = i - 1
        temp = S[i]
        while j >= 0 and temp < S[j]:
            S[j+1] = S[j]
            j -= 1
        S[j+1] = temp


def bucketsort(S, mutable_sort_method=insertion_sort):
    """
    bucketsort implementation with brute-force part sorting done with insertion-sort by default.
    """
    max_val = max(S)
    ratio = max_val / len(S)
    buckets = [[] for _ in range(len(S))]

    for i in range(len(S)):
        index = int(S[i] / ratio)
        if S[i] == max_val:
            buckets[-1].append(S[i])
        else:
            buckets[index].append(S[i])

    for bucket in buckets:
        mutable_sort_method(bucket)

    return sum(buckets, [])
