"""
C-14.56 Tamarindo University and many other schools worldwide are doing a joint
project on multimedia. A computer network is built to connect these
schools using communication links that form a tree. The schools decide
to install a file server at one of the schools to share data among all the
schools. Since the transmission time on a link is dominated by the link
setup and synchronization, the cost of a data transfer is proportional to the
number of links used. Hence, it is desirable to choose a “central” location
for the file server. Given a tree T and a node v of T, the eccentricity of v
is the length of a longest path from v to any other node of T. A node of T
with minimum eccentricity is called a center of T.
a. Design an efficient algorithm that, given an n-node tree T, computes
a center of T.
b. Is the center unique? If not, how many distinct centers can a tree
have?
"""

from copy import deepcopy

def tree_center(g):
    """
    returns tree center/bicenter with minimal eccentricity
    """
    g_cpy = deepcopy(g) # O(n+m)

    while g_cpy.vertex_count() > 1:
        if g_cpy.vertex_count() == 2:
            it = iter(iter(g_cpy.vertices()))
            v1 = next(it)
            v2 = next(it)
            e = next(iter(g_cpy.edges()))
            if set(e.endpoints()) == {v1, v2}:
                break
        to_remove = [v for v in g_cpy.vertices() if g_cpy.degree(v) == 1]
        for v in to_remove:
            g_cpy.remove_vertex(v)

    centers = [v.element() for v in g_cpy.vertices()]
    return {v for v in g.vertices() if v.element() in centers}


if __name__ == "__main__":
    from shared_14_chapter import Graph

    g = Graph()
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')

    e1 = g.insert_edge(v1, v2, 'e1')
    e2 = g.insert_edge(v2, v3, 'e2')

    center = tree_center(g)
    assert center == {v2}


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

    center = tree_center(g)
    assert center == {v2}


    g = Graph()
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    v4 = g.insert_vertex('v4')
    v5 = g.insert_vertex('v5')
    v6 = g.insert_vertex('v6')
    v7 = g.insert_vertex('v7')
    v8 = g.insert_vertex('v8')

    e1 = g.insert_edge(v1, v3, 'e1')
    e2 = g.insert_edge(v2, v3, 'e2')
    e3 = g.insert_edge(v2, v4, 'e3')
    e4 = g.insert_edge(v2, v5, 'e4')
    e5 = g.insert_edge(v3, v6, 'e5')
    e6 = g.insert_edge(v5, v7, 'e6')
    e7 = g.insert_edge(v7, v8, 'e7')

    center = tree_center(g)
    assert center == {v2, v5}


    g = Graph()
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    v4 = g.insert_vertex('v4')
    v5 = g.insert_vertex('v5')
    v6 = g.insert_vertex('v6')
    v7 = g.insert_vertex('v7')

    e1 = g.insert_edge(v1, v3, 'e1')
    e2 = g.insert_edge(v2, v3, 'e2')
    e3 = g.insert_edge(v2, v4, 'e3')
    e4 = g.insert_edge(v2, v5, 'e4')
    e5 = g.insert_edge(v3, v6, 'e5')
    e6 = g.insert_edge(v5, v7, 'e6')

    center = tree_center(g)
    assert center == {v2}
