"""
Design a variation of binary search for performing the multi-map operation find_all(k) implemented
with a sorted search table that includes duplicates, and show that it runs in O(s+logn) where
n is the number of elements in the dictionary and s is the number of items with given key k.
"""


def bin_search(seq, k, low=0, high=None):
    if high is None:
        high = len(seq)-1

    if high < low:
        return high + 1
    else:
        mid = (high + low) // 2
        if seq[mid] < k:
            return bin_search(seq, k, mid+1, high)
        else:
            return bin_search(seq, k, low, mid-1)

def find_all(seq, k):
    j = bin_search(seq, k) # find first
    result = [j]

    for i in range(j-1, 0, -1): # search left of key
        if seq[i] == k:
            result.append(i)
        else:
            break

    for i in range(j+1, len(seq)): # search right of key
        if seq[i] == k:
            result.append(i)
        else:
            break

    return result

if __name__ == "__main__":
    import random

    n = 10 # num of els for testing

    test_seq = random.sample(range(0, 100), n-1)
    test_seq.sort()
    lookup_idx = random.randint(0, n-1)
    lookup_el = test_seq[lookup_idx]
    test_seq.insert(lookup_idx+1, lookup_el) # make sure there's a duplicate

    print(f'searching sequence: {test_seq}')
    print(f'searching key: {lookup_el}')

    actual_indexes = find_all(test_seq, lookup_el)

    print(f'assert:{[lookup_idx, lookup_idx+1]} == {actual_indexes}')
    assert [lookup_idx, lookup_idx+1] == actual_indexes

