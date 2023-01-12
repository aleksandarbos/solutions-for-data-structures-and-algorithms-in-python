import py_compile
from lxml import etree as et


def print_toc(el, d, path):
    label = '.'.join(str(idx + 1) for idx in path)
    print(d*2*' ' + label + ' ' + el.tag)
    path.append(0)

    for c in el.iterchildren():
        print_toc(c, d+1, path)
        path[-1] += 1

    path.pop()

path = []
tree = et.parse('./input/trees/bookstore.xml')
print_toc(tree.getroot(), 0, path)
