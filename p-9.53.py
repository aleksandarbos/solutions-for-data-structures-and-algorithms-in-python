"""
Implement the in-place heap-sort algorithm. (array based heap)
"""

def parent(j):
    return (j-1) // 2

def left(j):
    return 2*j+1

def right(j):
    return 2*j+2

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def has_left(data, j):
    return left(j) < len(data)

def has_right(data, j):
    return right(j) < len(data)

def upheap(data, j):
    """
    array based recursive impl of upheap
    """
    p = parent(j)

    node_val = data[j]
    parent_val = data[p]

    if j > 0 and parent_val > node_val:
        swap(data, p, j)
        upheap(data, p)

def upheap_max(data, j):
    """
    array based recursive impl of upheap_max
    """
    p = parent(j)

    node_val = data[j]
    parent_val = data[p]

    if j > 0 and parent_val < node_val:
        swap(data, p, j)
        upheap_max(data, p)


def downheap(data, j):
    """
    array based recursive impl of downheap
    """
    if has_left(data, j):
        min_node = l_node = left(j)
        node_val = data[j]
        l_node_val = data[l_node]

        if has_right(data, j):
            r_node = right(j)
            r_node_val = data[r_node]

            if r_node_val < l_node_val:
                min_node = r_node

        min_node_val = data[min_node]

        if node_val > min_node_val:
            swap(data, j, min_node)
            downheap(data, min_node)

def downheap_max(data, j, stop_idx=None):
    """
    Array based recursive implementation of max oriented down-heap with the ability to stop
    bubbling at the given index position.

    Parameters
    ----------
    j: int
        position at which down heap bubbling should start at.
    stop_idx: int
        indicates at which index position down heap bubbling should stop at.
    """
    stop_idx = stop_idx or len(data)

    if has_left(data, j):
        max_node = l_node = left(j)
        node_val = data[j]
        l_node_val = data[l_node]

        if l_node >= stop_idx:
            return

        if has_right(data, j) and stop_idx > 2:
            r_node = right(j)
            r_node_val = data[r_node]

            if r_node >= stop_idx:
                return
            elif r_node_val > l_node_val:
                max_node = r_node

        max_node_val = data[max_node]

        if node_val < max_node_val:
            swap(data, j, max_node)
            downheap_max(data, max_node, stop_idx)

def heapify_max(data):
    start = parent(len(data)-1)
    for i in range(start, -1, -1):
        downheap_max(data, i)

def heapify(data):
    start = parent(len(data)-1)
    for i in range(start, -1, -1):
        downheap(data, i)

def heap_sort(array):
    """
    impl of the heap sort algorithm for the given array.

    Complexity:
        O(nlogn) => n times called O(logn) downheap_max.
    """
    heapify_max(array) # O(n) bottom-up max heap construction

    for i in range(len(array)-1, 0, -1): # O(n)
        swap(array, 0, i) # O(1)
        downheap_max(array, 0, stop_idx=i) # O(logn)

if __name__ == "__main__":
    import random

    A = [random.randint(0, 50) for i in range(0, 20)]
    B = A[:]

    print(f'before heap-sort, A: {A}')
    heap_sort(A)
    print(f'after heap-sort, A: {A}')

    assert A == sorted(B)
