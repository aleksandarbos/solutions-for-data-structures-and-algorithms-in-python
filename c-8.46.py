"""
the path length of a tree T is the sum of the depths of all positions in T.
describe a liner-time method for computing the path length of a tree T.
"""



def iter_depth_all(el, d):
    yield d
    for c in el.iterchildren():
        yield from iter_depth_all(c, d+1)


if __name__ == "__main__":
    from lxml import etree as et

    tree = et.parse('./input/trees/bin_tree_1.xml')
    root = tree.getroot()
    path_length = sum(iter_depth_all(root, 0)) # iter_depth_all results in O(n) and sum is another O(n) iteration
    print(f'path length of tree is: {path_length}') # of the given result therefore => O(2n) => 2*O(n) => O(n)
