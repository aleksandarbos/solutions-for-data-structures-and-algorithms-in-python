"""
write an algorithm which counts num of leaves in tree
"""

from lxml import etree as et


# impl made using the mutable list
def count_leaves_1(el, lst):
    if len(el) == 0:
        lst.append(1)
    for e in el.iterchildren():
        count_leaves_1(e, lst)

lst = []
tree = et.parse('./input/trees/bin_tree_1.xml')
count_leaves_1(tree.getroot(), lst)
print(f'count_leaves_1: {len(lst)}')

# ----------

def count_leaves_2(el):
    if len(el) == 0:
        return 1
    else:
        s = 0
        for e in el.iterchildren():
            s += count_leaves_2(e)
        return s

print(f'count_leaves_2: {count_leaves_2(tree.getroot())}')


# ----------

def count_leaves_3(el):
    if len(el) == 0:
        return 1
    else:
        return sum(count_leaves_3(e) for e in el.iterchildren())

print(f'count_leaves_3: {count_leaves_3(tree.getroot())}')
