import py_compile
from lxml import etree as et


def print_parenthic_str(el):
    print(el.tag, end='')

    if len(el) != 0:
        first_time=True
        for c in el.iterchildren():
            sep = f'( ' if first_time else ', '
            print(sep, end='')
            first_time = False
            print_parenthic_str(c)
        print(')', end='')

tree = et.parse('./input/trees/bookstore.xml')
print_parenthic_str(tree.getroot())
