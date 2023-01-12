"""
show how to use euler tour to impl f(p)
"""

from lxml import etree as et


def euler_tour(el, d, path):
    hook_previsit(el, d, path)
    results = []    # this line cleans results of children once parent traversal is completed
    path.append(0)

    for c in el.iterchildren():
        results.append(euler_tour(c, d+1, path))
        path[-1] += 1

    path.pop()
    answer = hook_postvisit(el, d, path, results)
    return answer


def euler_tour_1(el, d, path, results):
    """modified to keep track of all results from all postvisits adding external parameter reference.
    this can be also achieved by forming a new list and passing it as a parameter to the next
    recursive call, but that's inefficient.
    """
    hook_previsit(el, d, path)
    path.append(0)

    for c in el.iterchildren():
        results.append(euler_tour_1(c, d+1, path, results))
        path[-1] += 1

    path.pop()
    answer = hook_postvisit(el, d, path, results)
    return answer


def hook_previsit(el, d, path):
    pass

def hook_postvisit(el, d, path, results):
    import pdb; pdb.set_trace()
    return f'result of {el} with id {id(el)}'


results=[]
tree = et.parse('./input/trees/bin_tree_1.xml')
euler_tour_1(tree.getroot(), 0, [], results)
