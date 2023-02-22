"""
C-14.55 The time delay of a long-distance call can be determined by multiplying
a small fixed constant by the number of communication links on the telephone
network between the caller and callee. Suppose the telephone net-
work of a company named RT&T is a tree. The engineers of RT&T want
to compute the maximum possible time delay that may be experienced in
a long-distance call. Given a tree T, the diameter of T is the length of
a longest path between two nodes of T. Give an efficient algorithm for
computing the diameter of T.
"""

from shared_14_chapter import construct_path

def bfs(g, u, discovered):
    """
    modified bfs which adds level number next to each discovered node
    """
    level = [u]
    lvl_cnt = 1

    while len(level) > 0:
        next_level = []
        for v in level:
            for e in g.incident_edges(v):
                w = e.opposite(v)
                if w not in discovered:
                    discovered[w] = (e, lvl_cnt)
                    next_level.append(w)
        level = next_level
        if level != []:
            lvl_cnt += 1
    return lvl_cnt

def tree_diameter_path(g):
    """
    calculates the longest path between two nodes within a tree by doing
    bfs at leaf nodes (excluding their siblings).
    """
    leaves = []
    leave_parents = set()
    for v in g.vertices():
        edges = list(g.incident_edges(v))
        if len(edges) == 1:
            e = edges[0]
            origin, dest = e.endpoints()
            if dest == v and origin not in leave_parents: # gets one leaf per parent
                leaves.append(v)
                leave_parents.add(origin)

    discovered = {}
    max_lvl = 0
    diameter_pair = (None, None)
    for l in leaves:
        lvl = bfs(g, l, discovered) -1 # there's one extra loop
        if lvl > max_lvl:
            max_lvl = lvl
            # pick one (it's same path length for all siblings)
            furthest_node = next(k for k,v in discovered.items() if v[1] == lvl)
            diameter_pair = l, furthest_node
    return construct_path(g, *diameter_pair, discovered)


if __name__ == "__main__":
    from shared_14_chapter import Graph

    g = Graph()
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')

    e1 = g.insert_edge(v1, v2, 'e1')
    e2 = g.insert_edge(v2, v3, 'e2')

    path = tree_diameter_path(g)
    assert len(path) == 2


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
    v14 = g.insert_vertex('v14')
    v15 = g.insert_vertex('v15')

    e1 = g.insert_edge(v1, v2, 'e1')
    e2 = g.insert_edge(v2, v3, 'e2')
    e3 = g.insert_edge(v3, v4, 'e3')
    e4 = g.insert_edge(v3, v5, 'e4')
    e5 = g.insert_edge(v3, v6, 'e5')
    e6 = g.insert_edge(v2, v7, 'e6')
    e7 = g.insert_edge(v7, v8, 'e7')
    e8 = g.insert_edge(v8, v9, 'e8')
    e9 = g.insert_edge(v8, v10, 'e9')
    e10 = g.insert_edge(v10, v11, 'e10')
    e11 = g.insert_edge(v1, v12, 'e11')
    e12 = g.insert_edge(v12, v13, 'e12')
    e13 = g.insert_edge(v12, v14, 'e13')
    e14 = g.insert_edge(v14, v15, 'e14')

    path = tree_diameter_path(g)
    assert len(path) == 6
