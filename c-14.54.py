"""
C-14.54 A company named RT&T has a network of n switching stations connected
by m high-speed communication links. Each customer’s phone is directly
connected to one station in his or her area. The engineers of RT&T have
developed a prototype video-phone system that allows two customers to
see each other during a phone call. In order to have acceptable image
quality, however, the number of links used to transmit video signals be-
tween the two parties cannot exceed 4. Suppose that RT&T’s network is
represented by a graph. Design an efficient algorithm that computes, for
each station, the set of stations it can reach using no more than 4 links.
"""

from collections import deque

def bfs(g, u, max_lvl=None):
    """
    bfs using fifo queue extended with max_lvl indicator
    at which level to stop the search
    """
    level = [u]
    discovered = set()
    lvl_cnt = 0

    while len(level) > 0:
        if max_lvl is not None and lvl_cnt >= max_lvl:
            break
        next_level = []
        for v in level:
            for e in g.incident_edges(v):
                w = e.opposite(v)
                if w not in discovered and w != u:
                    discovered.add(w)
                    next_level.append(w)
        level = next_level
        lvl_cnt += 1
    return discovered


def find_closest_stations(g, n=4):
    """
    calculates set of stations for each node no further than `n` links
    """
    result = {}
    for v in g.vertices():
        result[v] = bfs(g, v, max_lvl=n)
    return result


if __name__ == "__main__":
    from shared_14_chapter import Graph

    g = Graph()
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    v4 = g.insert_vertex('v4')
    v5 = g.insert_vertex('v5')
    v6 = g.insert_vertex('v6')
    v7 = g.insert_vertex('v7')
    v8 = g.insert_vertex('v8')
    v9 = g.insert_vertex('v9')
    v10 = g.insert_vertex('v10')
    v11 = g.insert_vertex('v11')
    v12 = g.insert_vertex('v12')
    v13 = g.insert_vertex('v13')

    e1 = g.insert_edge(v2, v6, 'e1')
    e2 = g.insert_edge(v6, v3, 'e2')
    e3 = g.insert_edge(v6, v7, 'e3')
    e4 = g.insert_edge(v6, v9, 'e4')
    e5 = g.insert_edge(v9, v10, 'e5')
    e6 = g.insert_edge(v1, v10, 'e6')
    e7 = g.insert_edge(v9, v11, 'e7')
    e8 = g.insert_edge(v9, v8, 'e8')
    e9 = g.insert_edge(v7, v8, 'e9')
    e10 = g.insert_edge(v7, v4, 'e10')
    e11 = g.insert_edge(v8, v5, 'e11')
    e12 = g.insert_edge(v8, v12, 'e12')
    e13 = g.insert_edge(v11, v8, 'e13')
    e14 = g.insert_edge(v11, v13, 'e14')

    max_links = 4
    result = find_closest_stations(g, max_links)
    v1_reachable = g.vertices().difference([v1, v4]) # exclude self and point out of reach
    assert v1_reachable == result[v1]

    max_links = 1
    result = find_closest_stations(g, max_links)
    assert result[v10] == {v1, v9}
    assert result[v9] == {v10, v6, v11, v8}
