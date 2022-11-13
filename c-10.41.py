"""
Suppose we're given two sorted search tables S and T, each with n entries (with S and T
being implemented with arrays). Describe an O(log^2(n))-time algorithm for finding k-th smallest
key in the union of the keys from S and T (assuming no duplicates).

C-10.41 - Give an O(logn)-time solution for the previous problem.
"""

def kth_el_of_sorted_arrays(A, B, k):
    """
    gives k-th element of two sorted arrays A and B in O(log(len(A)) + log(len(B)))
    """
    def kth(A, B, l1, l2, h1, h2, k):

        # base case
        if l1 > h1:
            return B[l2+k-1]
        elif l2 > h2:
            return A[l1+k-1]

        mid1 = (h1+l1) // 2
        mid2 = (h2+l2) // 2
        kc = (mid1-l1+1) + (mid2-l2+1)

        if kc <= k:
            if A[mid1] < B[mid2]:
                # solution can't be in A[:mid1+1]
                return kth(A, B, mid1+1, l2, h1, h2, k-(mid1-l1+1))
            else:
                # solution can't be in B[:mid2+1]
                return kth(A, B, l1, mid2+1, h1, h2, k-(mid2-l2+1))
        else:
            if A[mid1] < B[mid2]:
                # solution can't be in B[mid2:]
                return kth(A, B, l1, l2, h1, mid2-1, k)
            else:
                # solution can't be in A[mid1:]
                return kth(A, B, l1, l2, mid1-1, h2, k)
    return kth(A, B, 0, 0, len(A)-1, len(B)-1, k)

if __name__ == "__main__":
    A = [2, 3, 6, 7, 9]
    B = [1, 4, 8, 10]

    assert kth_el_of_sorted_arrays(A, B, 5) == 6


