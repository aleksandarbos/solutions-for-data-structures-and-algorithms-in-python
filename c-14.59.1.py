"""
C-14.59 Design an efficient algorithm for finding a longest directed path from a
vertex s to a vertex t of an acyclic weighted directed graph G . Specify the
graph representation used and any auxiliary data structures used. Also,
analyze the time complexity of your algorithm.
"""

from shared_14_chapter import topological_sort

def longest_path(g, s, t):
    path = []
    tsort = topological_sort(g)
    longest = [-float('inf')] * len(tsort)
    longest[tsort.index(s)] = 0

    for v in tsort:
        for e in g.incident_edges(v, outgoing=False):
            u = e.opposite(v)
            old_length = longest[tsort.index(v)]
            new_length = longest[tsort.index(u)] + e.element()
            if new_length > old_length:
                path.append(e)
                longest[tsort.index(v)] = new_length
    return path

if __name__ == "__main__":
    from shared_14_chapter import Graph

    g = Graph(directed=True)
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    v4 = g.insert_vertex('v4')
    v5 = g.insert_vertex('v5')

    e1 = g.insert_edge(v1, v2, 3)
    e2 = g.insert_edge(v2, v3, 2)
    e3 = g.insert_edge(v4, v2, 6)
    e4 = g.insert_edge(v3, v5, 7)
    e5 = g.insert_edge(v2, v5, 5)
    e6 = g.insert_edge(v4, v5, 6)

    path = longest_path(g, v1, v5)
    assert path == [e1, e2, e4]
