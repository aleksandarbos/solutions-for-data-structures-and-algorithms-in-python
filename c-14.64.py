"""
C-14.64 Our implementation of shortest path lengths in Code Fragment 14.13
relies on use of “infinity” as a numeric value, to represent the distance bound
for vertices that are not (yet) known to be reachable from the source.
Reimplement that function without such a sentinel, so that vertices, other
than the source, are not added to the priority queue until it is evident that
they are reachable.
"""

from heapq import heappop, heappush
from shared_14_chapter import dijkstra as dijkstra_org, Graph

def dijkstra(g, src):
    d = {}
    d[src] = 0
    cloud = {}
    dummy = 0
    h = [(0, dummy, src)]

    while len(h) > 0:
        d_w, _, v = heappop(h)
        cloud[v] = d_w

        for e in g.incident_edges(v):
            u = e.opposite(v)
            wgt = e.element()

            if u not in cloud:
                # if discoverable add it to the heap
                entry = next((e for e in h if e[2] == u), None)
                if entry is None:
                    d[u] = d[v] + wgt
                    dummy += 1 # added bc for heap sorting
                    heappush(h, (d[u], dummy, u))

                if d[v] + wgt < d[u]:
                    d[u] = d[v] + wgt
                    del h[h.index(entry)]
                    heappush(h, (d[u], entry[1], u))
    return cloud


if __name__ == "__main__":
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

    d = dijkstra(g, v1)
    d_org = dijkstra_org(g, v1)
    assert all({d_org[k] == d[k] for k,v in d_org.items() if v != float('inf')})

