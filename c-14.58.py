"""
C-14.58 Let G be a weighted directed graph with n vertices. Design a variation
of Floyd-Warshall's algorithm for computing the lengths of the shortest
paths from each vertex to every other vertex in O(n^3) time.
"""

from copy import deepcopy

def floyd_warshall(g):
    """
    code fragment: 14.10 * modified to support weights *
    """
    closure = deepcopy(g)
    v_lst = list(closure.vertices())
    n = len(v_lst)

    for k in range(n):
        for i in range(n):
            e_to = closure.get_edge(v_lst[i], v_lst[k])
            if k != i and e_to is not None:
                for j in range(n):
                    e_from = closure.get_edge(v_lst[k], v_lst[j])
                    if i != j != k and e_from is not None:
                        e_trans = closure.get_edge(v_lst[i], v_lst[j])
                        trans_weight = e_to.element() + e_from.element()
                        if e_trans is None:
                            closure.insert_edge(v_lst[i], v_lst[j], trans_weight)
                        elif e_trans.element() > trans_weight: # replace if shorter way
                            closure.remove_edge(e_trans)
                            closure.insert_edge(v_lst[i], v_lst[j], trans_weight)
    return closure, v_lst

if __name__ == "__main__":
    from shared_14_chapter import Graph

    g = Graph(directed=True)
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    v4 = g.insert_vertex('v4')
    v5 = g.insert_vertex('v5')
    v6 = g.insert_vertex('v6')
    v7 = g.insert_vertex('v7')
    v8 = g.insert_vertex('v8')

    e1 = g.insert_edge(v1, v2, 10)
    e2 = g.insert_edge(v1, v5, 10)
    e3 = g.insert_edge(v4, v5, 15)
    e4 = g.insert_edge(v4, v6, 15)
    e5 = g.insert_edge(v2, v5, 10)
    e6 = g.insert_edge(v5, v6, 10)
    e7 = g.insert_edge(v2, v3, 5)
    e8 = g.insert_edge(v3, v7, 5)
    e9 = g.insert_edge(v6, v7, 13)
    e10 = g.insert_edge(v7, v8, 7)
    e11 = g.insert_edge(v6, v8, 15)
    e12 = g.insert_edge(v2, v8, 20)
    e13 = g.insert_edge(v5, v7, 2)

    closure, vertices = floyd_warshall(g)
    vertices.sort(key=lambda x: x.element())
    assert closure.get_edge(vertices[1], vertices[7]).element() == 17 # v2 -> v8
    assert closure.get_edge(vertices[0], vertices[7]).element() == 19 # v1 -> v8
