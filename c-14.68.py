"""
C-14.68 Consider a diagram of a telephone network, which is a graph G
whose vertices represent switching centers, and whose edges represent
communication lines joining pairs of centers. Edges are marked by their bandwidth,
and the bandwidth of a path is equal to the lowest bandwidth among the
path's edges. Give an algorithm that, given a network and two switching
centers a and b, outputs the maximum bandwidth of a path between a and b.
"""

from collections import deque
from shared_14_chapter import find_all_paths_bfs

def max_bandwidth(g, s, t):
    paths = find_all_paths_bfs(g, s, t)
    return max(min(map(lambda x:x.element(), p)) for p in paths)

if __name__ == "__main__":
    from shared_14_chapter import Graph

    g = Graph()
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')

    e1 = g.insert_edge(v1, v2, 4)
    e2 = g.insert_edge(v2, v3, 1)
    e3 = g.insert_edge(v1, v3, 3)

    src = v1
    target = v3
    assert max_bandwidth(g, src, target) == 3


    g = Graph()
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    v4 = g.insert_vertex('v4')

    e1 = g.insert_edge(v1, v2, 4)
    e2 = g.insert_edge(v2, v3, 1)
    e3 = g.insert_edge(v1, v3, 3)
    e4 = g.insert_edge(v3, v4, 2)
    e5 = g.insert_edge(v1, v4, 1)

    src = v1
    target = v4
    assert max_bandwidth(g, src, target) == 2
