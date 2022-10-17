from lxml import etree

tree = etree.parse("./input/trees/bookstore.xml")
root = tree.getroot()

def traverse(el):
    print(f'{el.tag} {el.text}')
    for e in el.iterchildren():
        traverse(e)

traverse(root)

