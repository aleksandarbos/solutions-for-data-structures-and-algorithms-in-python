"""
calculate the balance factor of the internal position p of the proper binary tree T.
balance factor is calculated as a difference between left and right subtrees of the position p.
show how to specialize Euler traversal to print out all balance factors for all internal positions
within the tree T.
"""

def euler_tour(el, d, path):
    """
    todo: finish this
    """
    results = [None, None]
    hook_previsit(el, d, path)

    left_c = el[0] if len(el) > 0 else None
    if left_c is not None:
        path.append(0)
        results[0] = euler_tour(left_c, d+1, path)
        path.pop()

    hook_invisit(el, d, path)

    right_c = el[1] if len(el) > 1 else None
    if right_c is not None:
        path.append(1)
        results[1] = euler_tour(right_c, d+1, path)
        path.pop()

    answer = hook_postvisit(el, d, path, results)
    return answer


def hook_previsit(el, d, path):
    pass

def hook_invisit(el, d, path):
    pass

def hook_postvisit(el, d, path, results):
    pass


def b_factor(el):
    """
    implementation w/o using euler traversal
    """
    if len(el) == 0:
        print(f'el: {el}, h: 0')
        return 0
    else:
        max = 0
        heights = []
        for c in el.iterchildren():
            h = b_factor(c)
            heights.append(h)
            if h > max:
                max = h
        balance_factor = heights[1] - heights[0]
        print(f'el: {el}, h: {1 + max}, balance factor: {balance_factor}')
        return 1 + max

if __name__ == "__main__":
    from lxml import etree as et

    tree = et.parse('./input/trees/bin_tree_1.xml')
    b_factor(tree.getroot())
