"""
Let T be a tree with n positions. Define the lowest common ancestor (LCA) between two
positions p and q as the lowest position in T that has both p and q as descendants
(where we allow a position to be descendant of itself). Given two positions p and q
describe an efficient algorithm for finding the LCA of p and q. What's running time
of your algorithm?
"""

from lxml import etree as et
from time import time

def lca(p, q):
    """
    returns lowest common ancestor for elements p and q
    """

    def iter_ancestors(el): # O(depth_el + 1)
        yield el
        parent = el.getparent()

        if parent is not None:
            yield from iter_ancestors(parent)

    ancestors = list(iter_ancestors(p)) # O(depth_p + 1)

    for ancestor in iter_ancestors(q): # O(depth_q)
        if ancestor in ancestors: # O(depth_q*depth_p) in worst case
            return ancestor


def lca2(p, q):
    """
    different implementation when ignoring generators
    """

    def iter_ancestors(el): # O(depth_el + 1)
        yield el
        parent = el.getparent()

        if parent is not None:
            yield from iter_ancestors(parent)

    p_ancestors = list(iter_ancestors(p)) # O(depth_p + 1)
    q_ancestors = list(iter_ancestors(q)) # O(depth_q + 1)

    for p_ancestor in p_ancestors: # O(depth_q)
        if p_ancestor in q_ancestors: # O(depth_q*depth_p) in worst case
            return p_ancestor



if __name__ == "__main__":
    tree = et.parse('./input/trees/bin_tree_1.xml')
    root = tree.getroot()
    p = root.xpath('//one_1[1]')[0]
    q = root.xpath('//one_2_2[1]')[0]

    low_cmn_ancestor = lca(p, q)
    print(f'lowest common ancestor for elements: p:{p} and q:{q} is: {low_cmn_ancestor}')


    n = 1000000
    print('benchmarking..')
    print(f'num of samples: {n}')

    print('lca...')
    t1 = time()
    for i in range(0, n):
        lca(p, q)
    print(f'elapsed time for lca: {time() - t1}')


    print('lca2...')
    t1 = time()
    for i in range(0, n):
        lca2(p, q)
    print(f'elapsed time for lca2: {time() - t1}')

"""
lowest common ancestor for elements: p:<Element one_1 at 0x187ca165d48> and q:<Element one_2_2 at 0x187ca165e48> is: <Element one at 0x187ca165ec8>
benchmarking..
num of samples: 1000000
lca...
elapsed time for lca: 3.7828524112701416
lca2...
elapsed time for lca2: 4.724111080169678
"""
