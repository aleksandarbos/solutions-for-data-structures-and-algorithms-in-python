"""
give an efficient algorithm that computes and prints for every position p of a tree T
the element of p followed by the height of the p's subtree
"""

from lxml import etree as et


def height_all(el):
    if len(el) == 0:
        print(f'el: {el}, h: 0')
        return 0
    else:
        max = 0
        for c in el.iterchildren():
            h = height_all(c)
            if h > max:
                max = h
        print(f'el: {el}, h: {1 + max}')
        return 1 + max

if __name__ == "__main__":
    tree = et.parse('./input/trees/bin_tree_1.xml')
    root = tree.getroot()
    print(height_all(root))
