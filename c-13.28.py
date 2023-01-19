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

    # 1D problem - distances from the start - in km :)
    holes = [3, 4, 5, 7, 9, 13, 14]
    k = 5 # num of km he can walk without refilling the bottle
    assert list(refill_strategy(holes, k)) == [5, 9, 14]

    """
    explanation: since Antatjari can go 5km without need to refill the water,
    he can go straight to 5km, therefore skipping watering holes located at 3 and 4km from
    the start. from position located at 5km away from start he can reach any position located at
    most 10km from start, the furthest watering hole lesser than 10km is the one at 9km.
    now starting at 9km + additional 5km after bottle refilling, he can go up to 14km and
    there's one located exactly 14km from the start.
    """


    holes = [3, 4, 5, 7, 9, 10, 13]
    k = 3
    assert list(refill_strategy(holes, k)) == [3, 5, 7, 10, 13]
