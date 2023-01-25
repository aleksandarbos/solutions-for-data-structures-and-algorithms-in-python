"""
make I(T) as a sum of all depths of internal positions in the tree T
make E(T) as a sum of all depths of external positions in the tree T
show that T is proper binary tree with n positions then when =>
    E(T) = I(T) + n - 1
"""

def preorder(el, d, internal_depths, external_depths):
    if len(el) == 0:
        external_depths.append(d)
    else:
        internal_depths.append(d)
        for c in el.iterchildren():
            preorder(c, d+1, internal_depths, external_depths)

if __name__ == "__main__":
    from lxml import etree as et

    internal_depths = []
    external_depths = []
    tree = et.parse('./input/trees/bin_tree_1.xml')
    root = tree.getroot()
    preorder(root, 0, internal_depths, external_depths)

    i_t = sum(internal_depths)
    e_t = sum(external_depths)

    n = len(root.xpath('.//*')) + 1 # plus root

    assert e_t == i_t + n - 1
