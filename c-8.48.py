"""
given a proper binary tree T define the reflection of T to be the binary tree T' such that each
node v in T is also in T' but the left child of v in T is v's right child in T' and the right child of v
in T is v's left child in T'. Show that preorder traversal of proper binary tree T is the same as postorder traversal
of T's reflection but in reverser order.
"""

from lxml import etree as et

def copy_tree(source_el, target_el=None):
    """
    imported copy tree from 'custom-8.9.py'
    """
    parent_el = target_el
    target_el = et.Element(source_el.tag, source_el.attrib)
    target_el.text = source_el.text

    if parent_el is not None:
        parent_el.insert(0, target_el) # tree reflection

    for src_el in source_el:
        copy_tree(src_el, target_el)
    return target_el

if __name__ == "__main__":
    tree1 = et.parse('./input/trees/bin_tree_1.xml')
    source_root = tree1.getroot()

    target_root = copy_tree(source_root)
    target_tree = et.ElementTree(target_root)


    print(et.tostring(target_tree, pretty_print=True).decode())

"""
<root>
  <two>
    <two_2>2.2 text</two_2><two_1>2.1 text</two_1></two><one>
    <one_2>
      <one_2_2>1.2.2 text</one_2_2><one_2_1>1.2.1 text</one_2_1></one_2><one_1>1.1 text</one_1></one></root>
"""
