"""
C-14.52 A graph G is bipartite if its vertices can be partitioned into two sets X and
Y such that every edge in G has one end vertex in X and the other in Y.
Design and analyze an efficient algorithm for determining if an undirected
graph G is bipartite (without knowing the sets X and Y in advance).
"""

from collections import deque

def is_bipartite(g, u):
    """
    checks if the graph `g` is bipartite, starting
    the discovery at vertex `u`.
    """
    colored = {k: -1 for k in g.vertices() if k != u}
    colored[u] = 0
    q = deque()
    q.append(u)

    while len(q) > 0:
        v = q.popleft()
        clr = colored[v]

        for e in g.incident_edges(v):
            vertex = e.opposite(v)
            vertex_clr = colored[vertex]

            if vertex_clr == clr:
                return False
            elif vertex_clr == -1:
                q.append(vertex)
                colored[vertex] = 1 if clr == 0 else 0
    return True

if __name__ == "__main__":
    from shared_14_chapter import Graph

    g = Graph()
    v1 = g.insert_vertex(element='v1')
    v2 = g.insert_vertex(element='v2')
    e1 = g.insert_edge(v1, v2, element='e1')
    assert is_bipartite(g, v1)

    g = Graph()
    v1 = g.insert_vertex(element='v1')
    v2 = g.insert_vertex(element='v2')
    v3 = g.insert_vertex(element='v3')
    e1 = g.insert_edge(v1, v2, element='e1')
    e2 = g.insert_edge(v1, v3, element='e2')
    e3 = g.insert_edge(v2, v3, element='e3')
    assert not is_bipartite(g, v1)

    g = Graph()
    v1 = g.insert_vertex(element='v1')
    v2 = g.insert_vertex(element='v2')
    v3 = g.insert_vertex(element='v3')
    v4 = g.insert_vertex(element='v4')
    v5 = g.insert_vertex(element='v5')
    v6 = g.insert_vertex(element='v6')
    v7 = g.insert_vertex(element='v7')
    v8 = g.insert_vertex(element='v8')
    e1 = g.insert_edge(v1, v2, element='e1')
    e2 = g.insert_edge(v2, v3, element='e2')
    e3 = g.insert_edge(v2, v4, element='e3')
    e4 = g.insert_edge(v3, v5, element='e4')
    e5 = g.insert_edge(v4, v6, element='e5')
    e6 = g.insert_edge(v5, v7, element='e6')
    e7 = g.insert_edge(v6, v7, element='e7')
    e8 = g.insert_edge(v7, v8, element='e8')
    assert is_bipartite(g, v1)


    g = Graph()
    v1 = g.insert_vertex(element='v1')
    v2 = g.insert_vertex(element='v2')
    v3 = g.insert_vertex(element='v3')
    v4 = g.insert_vertex(element='v4')
    v5 = g.insert_vertex(element='v5')
    v6 = g.insert_vertex(element='v6')
    v7 = g.insert_vertex(element='v7')
    e1 = g.insert_edge(v1, v2, element='e1')
    e2 = g.insert_edge(v2, v3, element='e2')
    e3 = g.insert_edge(v2, v4, element='e3')
    e4 = g.insert_edge(v3, v5, element='e4')
    e5 = g.insert_edge(v4, v6, element='e5')
    e6 = g.insert_edge(v5, v6, element='e6')
    e8 = g.insert_edge(v6, v7, element='e7')
    assert not is_bipartite(g, v1)
