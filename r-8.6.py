"""
write an algorithm which counts num of leaves which are left children of their
respective parents
"""

from lxml import etree as et

tree = et.parse('./input/trees/bin_tree_1.xml')

def count_left_leaves(el):
    if len(el) == 0 and el.getparent().index(el) == 0: # if it's left leaf
        return 1
    else:
        return sum(count_left_leaves(e) for e in el.iterchildren())

print(f'count_left_leaves: {count_left_leaves(tree.getroot())}')
