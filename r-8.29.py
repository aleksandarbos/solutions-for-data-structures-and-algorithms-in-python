"""
calculate the number of descendants for each node using euler traversal algorithm
"""



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
    if len (el) == 0:
        print(f'leaf: {el}, return: 0')
        return 0
    else:
        print(f'num of descendants of node {el} is: {len(results)}')
        return len(results)


if __name__ == "__main__":
    from lxml import etree as et

    results=[]
    tree = et.parse('./input/trees/bin_tree_1.xml')
    euler_tour_1(tree.getroot(), 0, [], results)
