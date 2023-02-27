"""
C-14.70 Inside the Castle of Asymptopia there is a maze, and along each corridor
of the maze there is a bag of gold coins. The amount of gold in each
bag varies. A noble knight, named Sir Paul, will be given the opportunity
to walk through the maze, picking up bags of gold. He may enter the
maze only through a door marked “ENTER” and exit through another
door marked “EXIT.” While in the maze he may not retrace his steps.
Each corridor of the maze has an arrow painted on the wall. Sir Paul may
only go down the corridor in the direction of the arrow. There is no way
to traverse a “loop” in the maze. Given a map of the maze, including the
amount of gold in each corridor, describe an algorithm to help Sir Paul
pick up the most gold.
"""

from shared_14_chapter import find_all_paths_bfs

def golden_path(g, start, exit):
    paths = find_all_paths_bfs(g, start, exit)
    best_path_idx = 0
    max_gold = 0

    for i, p in enumerate(paths):
        gold = sum(e.element() for e in p)
        if gold > max_gold:
            max_gold = gold
            best_path_idx = i
    return paths[best_path_idx]


if __name__ == "__main__":
    from shared_14_chapter import Graph

    g = Graph(directed=True)
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    # v4 = g.insert_vertex('v4')
    v5 = g.insert_vertex('v5')
    v6 = g.insert_vertex('v6')
    v7 = g.insert_vertex('v7')
    v8 = g.insert_vertex('v8')

    e1 = g.insert_edge(v1, v2, 10)
    e2 = g.insert_edge(v1, v5, 10)
    # e3 = g.insert_edge(v4, v5, 15)
    # e4 = g.insert_edge(v4, v6, 15)
    e5 = g.insert_edge(v2, v5, 10)
    e6 = g.insert_edge(v5, v6, 10)
    e7 = g.insert_edge(v2, v3, 5)
    e8 = g.insert_edge(v3, v7, 5)
    e9 = g.insert_edge(v6, v7, 13)
    e10 = g.insert_edge(v7, v8, 7)
    e11 = g.insert_edge(v6, v8, 15)
    e12 = g.insert_edge(v2, v8, 20)
    e13 = g.insert_edge(v5, v7, 2)

    assert golden_path(g, v1, v8) == [e1, e5, e6, e9, e10]
    assert sum(map(lambda x: x.element(), golden_path(g, v1, v8))) == 50
