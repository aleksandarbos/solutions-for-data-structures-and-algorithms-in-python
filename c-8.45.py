"""
give O(n) time algorithm for computing the depths of all positions of a tree
T where n is the number of nodes of T
"""



def depth_all(el, d):
    print(f'el: {el}, d: {d}')
    for c in el.iterchildren():
        depth_all(c, d+1)

if __name__ == "__main__":
    from lxml import etree as et

    tree = et.parse('./input/trees/bin_tree_1.xml')
    root = tree.getroot()
    print(depth_all(root, 0))
