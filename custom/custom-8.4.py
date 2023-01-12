from lxml import etree as et


def print_toc(el, d):
    print(d*2*' ' + el.tag)

    for c in el.iterchildren():
        print_toc(c, d+1)

tree = et.parse('./input/trees/bookstore.xml')
print_toc(tree.getroot(), 0)

