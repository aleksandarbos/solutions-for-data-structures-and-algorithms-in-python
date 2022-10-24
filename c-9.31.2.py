"""
impl of downheap of linked list tree
"""


def downheap_r(node):
    """
    recursive impl of downheap
    """
    if len(node) > 0:
        min_node = l_node = node[0]
        node_val = int(node.get('val'))
        l_node_val = int(l_node.get('val'))

        try:
            r_node = node[1]
            r_node_val = int(r_node.get('val'))

            if r_node_val < l_node_val:
                min_node = r_node
        except IndexError:
            pass

        min_node_val = int(min_node.get('val'))

        if node_val > min_node_val:
            node.set('val', str(min_node_val))
            min_node.set('val', str(node_val))

            downheap_r(min_node)


def downheap(node):
    """
    non-recursive impl
    """

    while len(node) > 0:
        min_node = l_node = node[0]
        node_val = int(node.get('val'))
        l_node_val = int(l_node.get('val'))

        try:
            r_node = node[1]
            r_node_val = int(r_node.get('val'))

            if r_node_val < l_node_val:
                min_node = r_node
        except IndexError:
            pass

        min_node_val = int(min_node.get('val'))

        if node_val < min_node_val:
            break
        else:
            node.set('val', str(min_node_val))
            min_node.set('val', str(node_val))

            node = min_node

if __name__ == "__main__":
    from lxml import etree as et
    from copy import deepcopy

    input_tree = './input/trees/unordered_heap_2.xml'
    tree = et.parse(input_tree)
    root = tree.getroot()
    root_2 = deepcopy(root)


    print(f'{input_tree} tree before downheap_r')
    print(et.tostring(root, pretty_print=True).decode())

    downheap_r(root)

    print(f'{input_tree} tree after downheap_r')
    print(et.tostring(root, pretty_print=True).decode())

    downheap(root_2)

    assert et.tostring(root) == et.tostring(root_2)
