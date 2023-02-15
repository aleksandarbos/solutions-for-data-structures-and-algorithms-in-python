"""
C-14.44 Write a function, components(g), for undirected graph g, that returns a
dictionary mapping each vertex to an integer that serves as an identifier for
its connected component. That is, two vertices should be mapped to the
same identifier if and only if they are in the same connected component.
"""

from shared_14_chapter import dfs

def components(g):
    tree_cnt = 0
    forest = {}

    for v in g.vertices():
        if v not in forest:
            tree = {v: tree_cnt}
            dfs(g, v, tree)
            for node in tree.keys():
                forest[node] = tree_cnt
            tree_cnt += 1
    return forest

if __name__ == "__main__":
    from shared_14_chapter import Graph

    g = Graph()
    v1 = g.insert_vertex(element='v1')
    v2 = g.insert_vertex(element='v2')
    v3 = g.insert_vertex(element='v3')
    e1 = g.insert_edge(v2, v3, element='e1')

    c = components(g)
    assert c[v1] == 1
    assert c[v2] == 0
    assert c[v3] == 0


    g = Graph()
    c = components(g)
    assert c == {}


    g = Graph()
    v1 = g.insert_vertex(element='v1')
    v2 = g.insert_vertex(element='v2')
    v3 = g.insert_vertex(element='v3')
    v4 = g.insert_vertex(element='v4')
    e1 = g.insert_edge(v1, v3, element='e1')
    e2 = g.insert_edge(v2, v4, element='e2')

    c = components(g)
    assert c[v1] == 0
    assert c[v3] == 0
    assert c[v2] == 1
    assert c[v4] == 1

