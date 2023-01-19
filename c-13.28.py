"""
A native Australian named Anatjari wishes to cross a desert carrying only
a single water bottle. He has a map that marks all the watering holes along
the way. Assuming he can walk k miles on one bottle of water, design an
efficient algorithm for determining where Anatjari should refill his bottle
in order to make as few stops as possible. Argue why your algorithm is
correct.
"""

def bin_search_lte(arr, x, left=0, right=None):
    """
    binary search less than or equal
    """
    right = right or len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            if mid == len(arr) - 1 or arr[mid + 1] > x:
                return mid
            else:
                left = mid + 1
        else:
            right = mid - 1
    return -1

def refill_strategy(holes, k):
    last_hole = 0
    holes.sort() # O(n*log(n))
    hole_idx = 0
    max_hole = holes[-1]

    while last_hole <= max_hole:
        hole_idx = bin_search_lte(holes, last_hole+k, hole_idx) # O(log(n))
        hole = holes[hole_idx]
        last_hole = hole
        yield hole
        if hole == max_hole:
            break

if __name__ == "__main__":
    holes = [3, 4, 5, 7, 9, 13, 14] # 1D problem
    k = 5
    assert list(refill_strategy(holes, k)) == [5, 9, 14]


    holes = [3, 4, 5, 7, 9, 10, 13] # 1D problem
    k = 3
    assert list(refill_strategy(holes, k)) == [3, 5, 7, 10, 13]
