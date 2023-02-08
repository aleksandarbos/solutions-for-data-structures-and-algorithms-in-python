"""
There are eight small islands in a lake, and the state wants to build seven
bridges to connect them so that each island can be reached from any other

one via one or more bridges. The cost of constructing a bridge is proportional
to its length. The distances between pairs of islands are given in the following table.

   1  2   3   4   5   6   7   8
1  - 240 210 340 280 200 345 120
2  -  -  265 175 215 180 185 155
3  -  -   -  260 115 350 435 195
4  -  - -  -  -  160 330 295 230
5  -  - - - -  -  -  360 400 170
6  -  - - - - - - -   -  175 205
7  -  - - - - - -  -  -   -  305
8  -  - - - - - - - - - - - - -
Find which bridges to build to minimize the total construction cost.
"""

from shared_14_chapter import prim_jarnik

def optimal_bridge_mst(g):
    return prim_jarnik(g)

if __name__ == "__main__":
    from shared_14_chapter import Graph, Vertex

    g = Graph()
    v = [g.insert_vertex(element=str(i+1)) for i, v in enumerate(range(8))]
    g.insert_edge(v[0], v[1], element=240)
    g.insert_edge(v[0], v[2], element=210)
    g.insert_edge(v[0], v[3], element=340)
    g.insert_edge(v[0], v[4], element=280)
    g.insert_edge(v[0], v[5], element=200)
    g.insert_edge(v[0], v[6], element=345)
    g.insert_edge(v[0], v[7], element=120)

    g.insert_edge(v[1], v[2], element=265)
    g.insert_edge(v[1], v[3], element=175)
    g.insert_edge(v[1], v[4], element=215)
    g.insert_edge(v[1], v[5], element=180)
    g.insert_edge(v[1], v[6], element=185)
    g.insert_edge(v[1], v[6], element=155)

    g.insert_edge(v[2], v[3], element=260)
    g.insert_edge(v[2], v[4], element=115)
    g.insert_edge(v[2], v[5], element=350)
    g.insert_edge(v[2], v[6], element=435)
    g.insert_edge(v[2], v[7], element=195)

    g.insert_edge(v[3], v[4], element=160)
    g.insert_edge(v[3], v[5], element=330)
    g.insert_edge(v[3], v[6], element=295)
    g.insert_edge(v[3], v[7], element=230)

    g.insert_edge(v[4], v[5], element=360)
    g.insert_edge(v[4], v[6], element=400)
    g.insert_edge(v[4], v[7], element=170)

    g.insert_edge(v[5], v[6], element=175)
    g.insert_edge(v[5], v[7], element=205)

    g.insert_edge(v[6], v[7], element=305)

    result = '[Edge[Vertex[2] ->[155] Vertex[7]], Edge[Vertex[2] ->[175] Vertex[4]], Edge[Vertex[4] ->[160] Vertex[5]], Edge[Vertex[3] ->[115] Vertex[5]], Edge[Vertex[5] ->[170] Vertex[8]], Edge[Vertex[1] ->[120] Vertex[8]], Edge[Vertex[6] ->[175] Vertex[7]]]'
    assert str(optimal_bridge_mst(g)) == result
