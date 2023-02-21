"""
C-14.53 An Euler tour of a directed graph G with n vertices and m edges is a
cycle that traverses each edge of G exactly once according to its direction.
Such a tour always exists if G is connected and the in-degree equals the
out-degree of each vertex in G . Describe an O(n+m)-time algorithm for
finding an Euler tour of such a directed graph G .
"""

from collections import defaultdict

def eulerian_cycle(g, u):
    """
    returns cycle path of the euler tour for strongly connected
    graph `g` assuming that each vertex `v` of graph `g` has the same
    in/out degree.
    """

    g_cpy = defaultdict(list) # O(n+m)
    for v in g.vertices():
        for e in g.incident_edges(v):
            g_cpy[v].append(e)

    s = [(u, None)]
    path = []

    while len(s) > 0:
        v, edge = s[-1]

        if g_cpy[v]:
            e = g_cpy[v].pop(0)
            w = e.opposite(v)
            s.append((w, e))
        else:
            if edge is not None:
                path.append(edge)
            s.pop()
    path.reverse()
    return path


if __name__ == "__main__":
    from shared_14_chapter import Graph

    g = Graph(directed=True)
    v1 = g.insert_vertex(element='v1')
    v2 = g.insert_vertex(element='v2')
    v3 = g.insert_vertex(element='v3')
    e1 = g.insert_edge(v1, v2, element='e1')
    e2 = g.insert_edge(v2, v3, element='e2')
    e3 = g.insert_edge(v3, v1, element='e3')

    path = eulerian_cycle(g, v1)
    assert path == [e1, e2, e3]


    g = Graph(directed=True)
    v1 = g.insert_vertex(element='v1')
    v2 = g.insert_vertex(element='v2')
    v3 = g.insert_vertex(element='v3')
    e1 = g.insert_edge(v1, v2, element='e1')
    e2 = g.insert_edge(v1, v3, element='e2')
    e3 = g.insert_edge(v2, v1, element='e3')
    e4 = g.insert_edge(v2, v3, element='e4')
    e5 = g.insert_edge(v3, v1, element='e5')
    e6 = g.insert_edge(v3, v2, element='e6')

    path = eulerian_cycle(g, v1)
    assert path == [e1, e3, e2, e6, e4, e5]

    g = Graph(directed=True)
    v1 = g.insert_vertex(element='v1')
    v2 = g.insert_vertex(element='v2')
    v3 = g.insert_vertex(element='v3')
    v4 = g.insert_vertex(element='v4')
    v5 = g.insert_vertex(element='v5')
    e1 = g.insert_edge(v1, v2, element='e1')
    e2 = g.insert_edge(v2, v3, element='e2')
    e3 = g.insert_edge(v3, v4, element='e3')
    e4 = g.insert_edge(v4, v2, element='e4')
    e5 = g.insert_edge(v2, v5, element='e5')
    e6 = g.insert_edge(v5, v1, element='e6')
    path = eulerian_cycle(g, v2)
    assert path == [e2, e3, e4, e5, e6, e1]
