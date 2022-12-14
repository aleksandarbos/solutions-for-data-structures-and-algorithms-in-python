"""
initial bucket-sort implementation
"""

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


if __name__ == "__main__":
    S = [51, -4, 11, 23, 0, -4, 9, 12, 1, 3, 3]
    assert bucketsort(S) == sorted(S)

    def selection_sort(seq):
        for i in range(len(seq)):
            min_idx = i
            for j in range(i, len(seq)):
                if seq[j] < seq[min_idx]:
                    min_idx = j
            seq[i], seq[min_idx] = seq[min_idx], seq[i]
        return seq

    assert bucketsort(S, mutable_sort_method=selection_sort) == sorted(S)
