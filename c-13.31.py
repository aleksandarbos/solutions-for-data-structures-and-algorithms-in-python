"""
In the art gallery guarding problem we are given a line L that represents
a long hallway in an art gallery. We are also given a set X = {x0,x1,...,xn-1}
of real numbers that specify the positions of paintings in this hallway.
Suppose that a single guard can protect all the paintings
within distance at most 1 of his or her position (on both sides). Design
an algorithm for finding a placement of guards that uses the minimum
number of guards to guard all the paintings with positions in X.
"""

def position_guards(X):
    """
    results with array of positions, where each position represents a guard and his position.
    """
    output = []
    paintings = []
    potential_guard = None
    old_len = 0

    for idx, pos in enumerate(X):
        potential_guard = potential_guard or pos
        min_reach, max_reach = pos - 1.0, pos + 1.0
        paintings = [pos]

        k = idx - 1                         # check +/- 1 radius of the position
        while k >= 0 and X[k] >= min_reach:
            paintings.append(X[k])
            k -= 1
        k = idx + 1
        while k < len(X) and X[k] <= max_reach:
            paintings.append(X[k])
            k += 1

        new_len = len(paintings)
        if new_len > old_len:
            potential_guard = pos
            old_len = new_len

        if k == idx + 1 and potential_guard is not None:
            output.append(potential_guard)
            potential_guard = None
            old_len = 0
    return output

if __name__ == "__main__":
    X = [0.5, 2.5, 2.9, 3.54, 6, 6.3, 6.95, 9, 10, 10.5, 10.9, 15, 20]
    guards = position_guards(X)
    num_of_guards = len(guards)
    assert guards == [0.5, 2.9, 6, 10, 15, 20]
    assert num_of_guards == 6

    X = [0.01, 0.62, 1.43, 4.49, 4.64, 5.22, 6.31, 7.22, 7.96, 9.55]
    guards = position_guards(X)
    num_of_guards = len(guards)
    assert guards == [0.62, 4.49, 7.22, 9.55]
    assert num_of_guards == 4

    X = [0]
    guards = position_guards(X)
    num_of_guards = len(guards)
    assert guards == [0]
    assert num_of_guards == 1
