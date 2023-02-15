"""
C-14.43 Implement an algorithm that returns a cycle in a directed graph G , if one
exists.
"""

def find_back_edge(g, node, discovered={}, path="0"):
    """
    finds first back edge during DFS traversal, returns None otherwise
    """
    for idx, e in enumerate(g.incident_edges(node)):
        new_path = path + str(idx)
        v = e.opposite(node)
        if v not in discovered:
            discovered[v] = (e, new_path)
            result = find_back_edge(g, v, discovered, new_path)
            if result is not None:
                return result
        else:
            _, v_path = discovered[v]
            if path.startswith(v_path): # v is ancestor of node
                return e

def construct_cycle_path(g, back_edge, discovered):
    """
    reconstructs the path of the cycle starting from the first discovered
    edge in the cycle found during DFS traversal to the last one.
    """
    cycle = [back_edge]
    start, end = back_edge.endpoints()

    walk = start
    while walk is not end:
        e, _ = discovered[walk]
        cycle.append(e)
        walk = e.opposite(walk)
    cycle.reverse()
    return cycle

def get_cycle(g, start_node, discovered):
    """
    starts DFS traversal and looks for back edge node, when first such is found
    it stops further DFS traversal and constructs the cycle path as an array of
    edges starting from the first to the last one discovered.
    """
    back_edge = find_back_edge(g, start_node, discovered)
    if back_edge is not None:
        return construct_cycle_path(g, back_edge, discovered)
    else:
        return []

if __name__ == "__main__":
    from shared_14_chapter import Graph

    g = Graph(directed=True)
    v1 = g.insert_vertex(element='v1')
    v2 = g.insert_vertex(element='v2')
    v3 = g.insert_vertex(element='v3')
    v4 = g.insert_vertex(element='v4')
    v5 = g.insert_vertex(element='v5')
    v6 = g.insert_vertex(element='v6')
    v7 = g.insert_vertex(element='v7')

    e1 = g.insert_edge(v1, v2, element='e1')
    e2 = g.insert_edge(v1, v3, element='e2')
    e3 = g.insert_edge(v3, v4, element='e3')
    e4 = g.insert_edge(v4, v5, element='e4')
    e5 = g.insert_edge(v5, v2, element='e5')
    e6 = g.insert_edge(v5, v6, element='e6')
    e7 = g.insert_edge(v6, v3, element='e7')

    discovered = {v1: (None, '0')}
    cycle = get_cycle(g, start_node=v1, discovered=discovered)
    assert cycle == [e3, e4, e6, e7]


    g = Graph(directed=True)
    v1 = g.insert_vertex(element='v1')
    v2 = g.insert_vertex(element='v2')
    v3 = g.insert_vertex(element='v3')
    e1 = g.insert_edge(v1, v2, element='e1')
    e2 = g.insert_edge(v1, v3, element='e2')
    e3 = g.insert_edge(v2, v3, element='e3')

    discovered = {v1: (None, '0')}
    cycle = get_cycle(g, start_node=v1, discovered=discovered)
    assert cycle == []
