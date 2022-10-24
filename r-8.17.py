
def euler_tour(el, d, path):
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

if __name__ == "__main__":
    from lxml import etree as et

    tree = et.parse('./input/trees/bin_tree_1.xml')
    euler_tour(tree.getroot(), 0, [])
