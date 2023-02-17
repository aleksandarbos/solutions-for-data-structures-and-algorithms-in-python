"""
C-14.51 Provide an implementation of the BFS algorithm that uses a FIFO queue,
rather than a level-by-level formulation, to manage vertices that have been
discovered until the time when their neighbors are considered.
"""

from collections import deque

def bfs(g, u, discovered):
    """
    bfs using fifo queue
    """
    q = deque()
    q.append(u)

    while len(q) > 0:
        print(q)
        v = q.popleft()
        for e in g.incident_edges(v):
            new_v = e.opposite(v)
            if new_v not in discovered:
                discovered[new_v] = e
                q.append(new_v)

if __name__ == "__main__":
    from shared_14_chapter import Graph

    g = Graph()
    v1 = g.insert_vertex(element='v1')
    v2 = g.insert_vertex(element='v2')
    v3 = g.insert_vertex(element='v3')
    v4 = g.insert_vertex(element='v4')
    v5 = g.insert_vertex(element='v5')
    e1 = g.insert_edge(v1, v2, element='e1')
    e2 = g.insert_edge(v1, v3, element='e2')
    e3 = g.insert_edge(v2, v3, element='e3')
    e4 = g.insert_edge(v3, v4, element='e4')
    e5 = g.insert_edge(v3, v5, element='e5')

    discovered = {v1: None}
    bfs(g, v1, discovered)
    assert len(discovered) == 5
