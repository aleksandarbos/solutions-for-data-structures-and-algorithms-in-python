"""
Computer networks should avoid single points of failure, that is, network
vertices that can disconnect the network if they fail. We say an undirected,
connected graph G is biconnected if it contains no vertex whose removal
would divide G into two or more connected components. Give an
algorithm for adding at most n edges to a connected graph G, with n ≥ 3
vertices and m ≥ n - 1 edges, to guarantee that G is biconnected. Your
algorithm should run in O(n+m) time.
"""

from shared_14_chapter import Graph

def create_biconnected_g(n):
    """
    This connects all the vertices in a cycle, which is itself biconnected.
    """
    g = Graph()
    prev_v = start_v = g.insert_vertex(element=0)
    for i in range(1, n):
        new_v = g.insert_vertex(element=i)
        if prev_v is not None:
            g.insert_edge(prev_v, new_v)
        prev_v = new_v
    g.insert_edge(prev_v, start_v)
    return g


if __name__ == "__main__":
    n = 5
    g = create_biconnected_g(n)
    assert g.edge_count() <= n

