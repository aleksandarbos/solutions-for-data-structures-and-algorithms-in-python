"""
write an algorithm which counts num of leaves which are left children of their
respective parents
"""

from lxml import etree as et


def count_left_leaves(el):
    if len(el) == 0 and el.getparent().index(el) == 0: # if it's left leaf
        return 1
    else:
        return sum(count_left_leaves(e) for e in el.iterchildren())


if __name__ == "__main__":
    tree = et.parse('./input/trees/bin_tree_1.xml')

    cnt_left_leaves = count_left_leaves(tree.getroot())
    assert cnt_left_leaves == 3
    print(f'count_left_leaves: {cnt_left_leaves}')
