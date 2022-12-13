"""
Suppose we are given two n-element sorted sequences A and B each with distinct elements, but
potentially some elements that are in both sequences. Describe an O(n)-time method for computing
a sequence representing the union A U B (with no duplicates) as a sorted sequence.
"""

def merge(A, B): # runs in O(len(A)+len(B))
    cnt_a, cnt_b = 0, 0
    result = []

    while cnt_a + cnt_b < len(A) + len(B):
        if cnt_b == len(B) or (cnt_a < len(A) and A[cnt_a] <= B[cnt_b]):
            if A[cnt_a] == B[cnt_b]: # ignore duplicate in B
                cnt_b += 1
            result.append(A[cnt_a])
            cnt_a += 1
        else:
            result.append(B[cnt_b])
            cnt_b += 1
    return result

if __name__ == "__main__":

    s1 = [1, 6, 7, 11]
    s2 = [0, 6, 7, 12]

    s = merge(s1, s2)
    assert s == [0, 1, 6, 7, 11, 12]
