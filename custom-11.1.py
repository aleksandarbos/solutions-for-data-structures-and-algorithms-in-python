"""
Find kth element in indexed binary search tree in O(h) worst time.
"""

def get(root, index):
    """
    gets element at `index` position from the binary search tree rooted at `root`.
    ref: https://www.cise.ufl.edu/~sahni/cop3530/slides/lec262.pdf (beautiful solution)
    """
    left_size = int(root.get('leftSize'))
    if left_size == index:
        return root
    elif left_size > index:
        return get(root[0], index)
    else:
        return get(root[1], index-left_size-1)

if __name__ == "__main__":
    from lxml import etree as et

    tree = et.parse('./input/trees/bst_1.xml')
    root = tree.getroot()

    el = get(root, index=6)
    assert el.get('val') == "16"

    el = get(root, index=10)
    assert el.get('val') == "34"

    el = get(root, index=0)
    assert el.get('val') == "0"
