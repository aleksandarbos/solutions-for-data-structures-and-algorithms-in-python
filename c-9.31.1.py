"""
give non-recursive impl of _upheap linked list tree
"""


def _upheap_r(node):
    """
    recursive impl of upheap
    """
    parent = node.getparent()
    node_val = int(node.get('val'))
    parent_val = int(parent.get('val')) if parent is not None else None

    if parent is not None and parent_val > node_val:
        node.set('val', str(parent_val))
        parent.set('val', str(node_val))
        _upheap_r(parent)

def _upheap(node):
    """
    non-recursive impl of upheap
    """
    parent = node.getparent()
    node_val = int(node.get('val'))
    parent_val = int(parent.get('val')) if parent is not None else None

    while parent is not None and parent_val > node_val:
        node.set('val', str(parent_val))
        parent.set('val', str(node_val))

        node = parent
        parent = parent.getparent()
        node_val = int(node.get('val'))
        parent_val = int(parent.get('val')) if parent is not None else None


def _upheap_2(node):
    """
    another non-recursive impl of upheap
    """

    while True:
        parent = node.getparent()
        node_val = int(node.get('val'))
        parent_val = int(parent.get('val')) if parent is not None else None

        if parent is None or parent_val < node_val:
            break

        node.set('val', str(parent_val))
        parent.set('val', str(node_val))

        node = parent
        parent = parent.getparent()

if __name__ == "__main__":
    from lxml import etree as et
    from copy import deepcopy

    input_tree = './input/trees/unordered_heap_1.xml'
    tree = et.parse(input_tree)
    root = tree.getroot()
    root_2 = deepcopy(root)
    root_3 = deepcopy(root)

    inserted_el = root.xpath('//node[@val="0"][1]')[0]
    inserted_el_2 = root_2.xpath('//node[@val="0"][1]')[0]
    inserted_el_3 = root_3.xpath('//node[@val="0"][1]')[0]


    print(f'{input_tree} tree before _upheap_r')
    print(et.tostring(root, pretty_print=True).decode())

    _upheap_r(inserted_el)

    print(f'{input_tree} tree after _upheap_r')
    print(et.tostring(root, pretty_print=True).decode())

    _upheap(inserted_el_2)
    _upheap_2(inserted_el_3)

    assert et.tostring(root) == et.tostring(root_2) == et.tostring(root_3)

