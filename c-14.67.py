"""
C-14.67 Let G be a graph with n vertices and m edges such that all the edge weights
in G are integers in the range [1,n]. Give an algorithm for finding a minimum spanning
tree for G in O(mlog*n) time.
"""

from shared_14_chapter import kruskal_mst, Graph

if __name__ == "__main__":
    g = Graph()
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    v4 = g.insert_vertex('v4')
    v5 = g.insert_vertex('v5')
    v6 = g.insert_vertex('v6')
    v7 = g.insert_vertex('v7')
    v8 = g.insert_vertex('v8')

    e1 = g.insert_edge(v1, v2, 4)
    e2 = g.insert_edge(v1, v5, 5)
    e3 = g.insert_edge(v4, v5, 7)
    e4 = g.insert_edge(v4, v6, 6)
    e5 = g.insert_edge(v2, v5, 5)
    e6 = g.insert_edge(v5, v6, 4)
    e7 = g.insert_edge(v2, v3, 2)
    e8 = g.insert_edge(v3, v7, 2)
    e9 = g.insert_edge(v6, v7, 6)
    e10 = g.insert_edge(v7, v8, 3)
    e11 = g.insert_edge(v6, v8, 7)
    e12 = g.insert_edge(v2, v8, 8)
    e13 = g.insert_edge(v5, v7, 1)

    tree = kruskal_mst(g)
    assert set(tree) == {e13, e8, e7, e10, e6, e1, e4}
