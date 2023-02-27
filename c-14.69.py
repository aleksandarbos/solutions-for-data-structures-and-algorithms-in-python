"""
C-14.69 NASA wants to link n stations spread over the country using
communication channels. Each pair of stations has a different bandwidth available,
which is known a priori. NASA wants to select n-1 channels (the minimum possible)
in such a way that all the stations are linked by the channels
and the total bandwidth (defined as the sum of the individual bandwidths
of the channels) is maximum. Give an efficient algorithm for this problem
and determine its worst-case time complexity. Consider the weighted
graph G = (V,E), where V is the set of stations and E is the set of
channels between the stations. Define the weight w(e) of an edge e in E as the
bandwidth of the corresponding channel.
"""

from shared_14_chapter import kruskal_mst

if __name__ == "__main__":
    from shared_14_chapter import Graph

    # issue can be resolved by defining G'=-G where all weights are
    # multiplied by -1, which will result in max-oriented mst.

    g = Graph()
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')

    e1 = g.insert_edge(v1, v2, -4)
    e2 = g.insert_edge(v2, v3, -1)
    e3 = g.insert_edge(v1, v3, -3)

    assert kruskal_mst(g) == [e1, e3]


    g = Graph()
    v1 = g.insert_vertex('v1')
    v2 = g.insert_vertex('v2')
    v3 = g.insert_vertex('v3')
    v4 = g.insert_vertex('v4')

    e1 = g.insert_edge(v1, v2, -4)
    e2 = g.insert_edge(v2, v3, -1)
    e3 = g.insert_edge(v1, v3, -3)
    e4 = g.insert_edge(v3, v4, -2)
    e5 = g.insert_edge(v1, v4, -1)

    assert kruskal_mst(g) == [e1, e3, e4]
