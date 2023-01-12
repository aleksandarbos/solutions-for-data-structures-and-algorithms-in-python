"""
make util for copying tree
"""

from lxml import etree as et

def copy_tree(source_el, target_el=None):
    parent_el = target_el
    target_el = et.Element(source_el.tag, source_el.attrib)
    target_el.text = source_el.text

    if parent_el is not None:
        parent_el.append(target_el)

    for src_el in source_el:
        copy_tree(src_el, target_el)
    return target_el

if __name__ == "__main__":
    tree1 = et.parse('./input/trees/bin_tree_1.xml')
    source_root = tree1.getroot()

    target_root = copy_tree(source_root)
    target_tree = et.ElementTree(target_root)


    print(et.tostring(target_tree, pretty_print=True).decode())
