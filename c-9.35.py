"""
Given a heap T and a key k, give an algorithm to compute all the entries in T having a key less
than or equal to k.
"""


def iter_lte(node, k):
    """
    yields keys of heap T which are less than or equal to key k
    """
    if int(node.get('val')) <= k:
        yield node.get('val')

    for c in node.iterchildren():
        yield from iter_lte(c, k)


if __name__ == "__main__":
    from lxml import etree as et

    tree = et.parse('./input/trees/heap_2.xml')
    T = tree.getroot()

    k = 9
    results = list(iter_lte(T, k))
    print(f'filtered values for key: {k} are: {results}')

    assert results == ['2', '5', '9', '9', '3']
