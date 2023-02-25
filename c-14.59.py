"""
C-14.59 Design an efficient algorithm for finding a longest directed path from a
vertex s to a vertex t of an acyclic weighted directed graph G . Specify the
graph representation used and any auxiliary data structures used. Also,
analyze the time complexity of your algorithm.

NOTE: dijkstra algorithm is failing with negative edges for certain edge cases
such as displayed in here: https://stackoverflow.com/a/8081947/5736491
"""

from heapq import heapify, heappop, heappush

def dijkstra(g, src):
    d = {}
    cloud = {}
    h = []
    dummy = 0

    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')
        h.append((d[v], dummy, v)) # adding dummy so `v` is never compared in radix sort
        dummy += 1
    heapify(h)

    while len(h) > 0:
        d_w, _, v = heappop(h)
        cloud[v] = d_w
        for e in g.incident_edges(v):
            u = e.opposite(v)
            if u not in cloud:
                entry = next((e for e in h if e[2] == u), None)
                wgt = e.element()
                if d[v] + wgt < d[u]:
                    d[u] = d[v] + wgt
                    del h[h.index(entry)]
                    heappush(h, (d[u], entry[1], u))
    return cloud

def construct_path(g, s, d):
    path = []
    for v in d:
        if v is not s:
            for e in g.incident_edges(v, outgoing=False):
                u = e.opposite(v)
                wgt = e.element()
                if d[v] == d[u] + wgt:
                    path.append(e)
    return path

def longest_path(g, s, t):
    d = dijkstra(g, s)
    return construct_path(g, s, d)


if __name__ == "__main__":
    from shared_14_chapter import Graph

    g = Graph(directed=True)
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    v4 = g.insert_vertex('v4')
    v5 = g.insert_vertex('v5')

    e1 = g.insert_edge(v1, v2, -3)
    e2 = g.insert_edge(v2, v3, -2)
    e3 = g.insert_edge(v4, v2, -6)
    e4 = g.insert_edge(v3, v5, -7)
    e5 = g.insert_edge(v2, v5, -5)
    e6 = g.insert_edge(v4, v5, -6)

    p = longest_path(g, v1, v5)
