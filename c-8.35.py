"""
define "isomorphic" algorithm which compares two trees t1 and t2. two trees are isomorphic if one condition is
satisfied: 1. both t1 and t2 are empty. 2. roots of t1 and t2 have same number k>=0 of subtrees and each i-th subtree
of t1 is isomorphic to the i-th subtree t2 for i=1,2,3...k
"""


def isomorphic(t1, t2):
    if len(t1) != len(t2):
        return False
    else:
        k = len(t1)
        for i in range(0, k):
            res = isomorphic(t1[i], t2[i])
            if res == False:
                return False
    return True

if __name__ == "__main__":
    from lxml import etree as et

    tree1 = et.parse('./input/trees/isomorphic_1.xml')
    t1 = tree1.getroot()

    tree2 = et.parse('./input/trees/isomorphic_2.xml')
    t2 = tree2.getroot()

    print(f'isomorphic(t1, t2): {isomorphic(t1, t2)}')
