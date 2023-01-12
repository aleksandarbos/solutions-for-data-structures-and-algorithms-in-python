from lxml import etree as et
from time import time

class Tree(object):

    def __init__(self, *args, **kwargs):
        input_path = kwargs.get('path')
        self.etree = et.parse(input_path)
        self.root = self.etree.getroot()

    def preorder(self):
        answer = []
        self._r_preorder(self.root, answer)
        return answer

    def _r_preorder(self, e, answer): # recursive fun is mutating answer list param
        answer.append(e)
        for c in e.iterchildren():
            self._r_preorder(c, answer)


if __name__ == "__main__":
    tree = Tree(path='./input/trees/bookstore.xml')
    # print([f'{e.tag} {e.text}' for e in t1.preorder()])

    t1 = time()
    for i in range(0, 1000000):
        tree.preorder()
    print(f'elapsed time: {time() - t1}')
