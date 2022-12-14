
def merge(A, B):
    """
    merges two ordered sequences of variable length. time complexity: O(len(A)+len(B))
    """
    count_a = 0
    count_b = 0

    if A == [] or B == []:
        raise Exception('Both A and B need to have at least one element.')

    while count_a < len(A) and count_b < len(B):
        if A[count_a] < B[count_b]:
            yield A[count_a]
            count_a += 1
        elif A[count_a] > B[count_b]:
            yield B[count_b]
            count_b += 1

    if count_a >= len(A):
        for i in range(count_b, len(B)):
            yield B[i]
    elif count_b >= len(B):
        for i in range(count_a, len(A)):
            yield A[i]

def find_kth_element(A, B, k):
    """
    finds k-th element of the two sorted arrays A and B.
    time complexity: O(k)
    """
    result = None
    for i, kth in enumerate(merge(A, B)):
        if i == k-1:
            result = kth
    return result

if __name__ == "__main__":
    A = [3, 5, 7, 9]
    B = [1, 4, 8, 11, 13, 16]

    C = list(merge(A, B))
    assert C == [1, 3, 4, 5, 7, 8, 9, 11, 13, 16]

    A = [0]
    B = [2]
    C = list(merge(A, B))
    assert C == [0, 2]

    A = [4]
    B = [1, 5, 6]
    C = list(merge(A, B))
    assert C == [1, 4, 5, 6]

    try:
        merge([], [0])
    except Exception as e:
        assert e is not None

    A = [3, 6, 9]
    B = [8]
    C = list(merge(A, B))
    assert C == [3, 6, 8, 9]

    A = [1, 3, 11]
    B = [4, 8] # C = [1, 3, 4, 8, 11]
    assert find_kth_element(A, B, k=3) == 4
    assert find_kth_element(A, B, k=1) == 1
    assert find_kth_element(A, B, k=5) == 11
