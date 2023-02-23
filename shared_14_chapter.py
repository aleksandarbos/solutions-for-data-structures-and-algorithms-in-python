"""
graph and graph related stuff
"""

from collections import deque

class Vertex(object):
    __slots__ = '_element'

    def __init__(self, element=None, *args, **kwargs):
        self._element = element

    def element(self):
        return self._element

    def __repr__(self):
        if hasattr(self, '_element') is not None:
            return f'Vertex[{self._element}]'
        else:
            return super().__repr__()

class Edge(object):
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, origin, destination, element=None, *args, **kwargs):
        self._origin = origin
        self._destination = destination
        self._element = element

    def element(self):
        return self._element

    def endpoints(self):
        return (self._origin, self._destination)

    def opposite(self, v):
        if v not in (self._origin, self._destination):
            raise Exception('Vertex is not an endpoint of this edge.')
        return self._destination if v == self._origin else self._origin

    def __repr__(self):
        if self._element is not None:
            return f'Edge[{self._origin} ->[{self._element}] {self._destination}]'
        else:
            return f'Edge[{self._origin} -> {self._destination}]'

class Graph(object):

    def __init__(self, directed=False, *args, **kwargs):
        self._outgoing = {}
        self._incoming = self._outgoing if not directed else {}

    def is_directed(self):
        return self._outgoing is not self._incoming

    def insert_vertex(self, element=None):
        v = Vertex(element)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, element=None):
        e = Edge(u, v, element)
        self._incoming[v][u] = e
        self._outgoing[u][v] = e
        return e

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for e in adj[v].values():
            yield e

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return set(self._outgoing.keys())

    def edge_count(self):
        s = sum([len(self._outgoing[v]) for v in self._outgoing])
        return s if self.is_directed() else s // 2

    def edges(self):
        edges = set()
        for v in self._outgoing:
            edges.update(self._outgoing[v].values())
        return edges

    def get_edge(self, u, v):
        return self._outgoing[u].get(v, None)

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def remove_vertex(self, v):
        """
        removes vertex `v` and it's related edges in O(deg(v)) amortized time.
        exercise: c-14.37.
        """
        outgoing_edges = list(self.incident_edges(v))
        incoming_edges = []
        if self.is_directed():
            incoming_edges = list(self.incident_edges(v, outgoing=False))
            if v in self._incoming:
                del self._incoming[v]
            for e in incoming_edges: # O(deg(v))
                u = e.opposite(v)
                del self._outgoing[u][v]
        if v in self._outgoing:
            del self._outgoing[v]
        for e in outgoing_edges: # O(deg(v))
            u = e.opposite(v)
            del self._outgoing[u][v]

    def remove_edge(self, e):
        """
        removes edge `e` from graph in O(1) time.
        exercise: c-14.38.
        """
        u, v = e.endpoints()

        del self._outgoing[u][v]
        if self.is_directed():
            del self._incoming[v][u]
        else:
            del self._outgoing[v][u]

def dfs(g, u, discovered={}):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e

def bfs(g, u, discovered):
    """
    bfs using fifo queue
    """
    q = deque()
    q.append(u)

    while len(q) > 0:
        v = q.popleft()
        for e in g.incident_edges(v):
            new_v = e.opposite(v)
            if new_v not in discovered:
                discovered[new_v] = e
                q.append(new_v)

def construct_path(g, end, start, discovered):
    """
    reconstructs the path from the vertex `start` to the `end` vertex using
    `discovered` discovery search map.
    """
    path = []

    walk = start
    while walk is not end:
        e, _ = discovered[walk]
        path.append(e)
        walk = e.opposite(walk)
    path.reverse()
    return path

def prim_jarnik(g):
    from heapq import heappush, heappop

    d = {}
    tree = []
    h = []

    # insertion counter bc Gods of Python won't make normal PriorityQueue class
    dummy = 0

    for v in g.vertices():
        if len(d) == 0:
            d[v] = 0
        else:
            d[v] = float('inf')
        dummy += 1
        heappush(h, (d[v], dummy, (v, None))) # dummy autoincr will make last tuple out of comparison

    while len(h) > 0:
        key, _, value = heappop(h)
        u, edge = value
        if edge is not None:
            tree.append(edge)
        for link in g.incident_edges(u):
            v = link.opposite(u)
            e = next((e for e in h if e[0] == d[v] and e[2][0] == v), None)
            if e is not None:
                wgt = link.element()
                if wgt < d[v]:
                    d[v] = wgt
                    del h[h.index(e)]
                    heappush(h, (d[v], e[1], (v, link)))
    return tree

def floyd_warshall(g):
    """
    code fragment: 14.10
    """
    from copy import deepcopy

    closure = deepcopy(g)
    v_lst = list(closure.vertices())
    n = len(v_lst)

    for k in range(n):
        for i in range(n):
            if k != i and closure.get_edge(v_lst[i], v_lst[k]) is not None:
                for j in range(n):
                    if i != j != k and closure.get_edge(v_lst[k], v_lst[j]) is not None:
                        if closure.get_edge(v_lst[i], v_lst[j]) is None:
                            closure.insert_edge(v_lst[i], v_lst[j])
    return closure

if __name__ == "__main__":
    # make a triangle shaped undirected cyclic graph
    g = Graph()
    v1 = g.insert_vertex(element='v1')
    v2 = g.insert_vertex(element='v2')
    v3 = g.insert_vertex(element='v3')

    e1 = g.insert_edge(v1, v2, element=10)
    e2 = g.insert_edge(v2, v3, element=20)
    e3 = g.insert_edge(v3, v1, element=30)

    assert g.edge_count() == 3
    assert g.vertex_count() == 3
    assert not g.is_directed()
    assert g.vertices() == {v1, v2, v3}
    assert g.edges() == {e1, e2, e3}
    assert list(g.incident_edges(v1)) == [e1, e3]
    assert g.degree(v1) == 2
    assert g.get_edge(v3, v1) == e3
    assert prim_jarnik(g) == [e2, e1]

    g.remove_vertex(v1)
    assert g.edges() == {e2}
    assert g.vertices() == {v2, v3}
    assert e2.endpoints() == (v2, v3)

    g.remove_edge(e2)
    assert g.edges() == set()

    # directed triangle graph v1 -> v2, v1 -> v3, v2 -> v3
    g_dir = Graph(directed=True)
    v1 = g_dir.insert_vertex(element='v1')
    v2 = g_dir.insert_vertex(element='v2')
    v3 = g_dir.insert_vertex(element='v3')

    e1 = g_dir.insert_edge(v1, v2, element=10)
    e2 = g_dir.insert_edge(v2, v3, element=20)
    e3 = g_dir.insert_edge(v1, v3, element=30)

    assert g_dir.edge_count() == 3
    assert g_dir.vertex_count() == 3
    assert g_dir.is_directed()

    g_dir.remove_vertex(v3)
    assert g_dir.edges() == {e1}
    assert g_dir.vertices() == {v1, v2}

    g_dir.remove_edge(e1)
    assert g_dir.edges() == set()
