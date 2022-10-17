from lxml import etree as et
from time import time

class Tree(object):

    def __init__(self, *args, **kwargs):
        input_path = kwargs.get('path')
        self.etree = et.parse(input_path)
        self.root = self.etree.getroot()

    def preorder(self):
        def _r_preorder(e):
            yield e
            for c in e.iterchildren():
                yield from _r_preorder(c)

        for c in _r_preorder(self.root):
            yield c


if __name__ == "__main__":
    tree = Tree(path='./input/trees/bookstore.xml')
    # print([f'{e.tag} {e.text}' for e in t1.preorder()])

    t1 = time()
    for i in range(0, 1000000):
        list(tree.preorder())
    print(f'elapsed time: {time() - t1}')
