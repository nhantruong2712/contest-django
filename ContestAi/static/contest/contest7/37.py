import networkx as nx
import time


def filter(n, b):
    if n[0] != b:
        return n[0]
    return n[1]


def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return True
    else:
        return False


def removeEdge(edges, n, m):
    try:
        edges.remove((n, m))
    except:
        try:
            edges.remove((m, n))
        except:
            return


def checkCycles(edges, edge):
    p0 = edge[0]
    p1 = edge[1]
    edgeOf_0 = [x for x in edges if (p0 in x)]
    edgeOf_1 = [x for x in edges if (p1 in x)]
    point_0 = list(map(lambda x: filter(x, p0), edgeOf_0))
    point_1 = list(map(lambda x: filter(x, p1), edgeOf_1))
    if p0 in point_1 or p1 in point_0 or common_member(point_1, point_0):
        return True
    for edge0 in edgeOf_0:
        for edge1 in edgeOf_1:
            if edge0[0] == p0:
                pn_0 = edge0[1]
            else:
                pn_0 = edge0[0]
            if edge1[0] == p1:
                pn_1 = edge1[1]
            else:
                pn_1 = edge1[0]
            temp_edges = edges.copy()
            removeEdge(temp_edges, p0, pn_0)
            removeEdge(temp_edges, p1, pn_1)
            if checkCycles(temp_edges, (pn_0, pn_1)):
                return True
    return False


def Kruskal(list_edges, list_edges_weight, numNode):
    edges = []
    long_run = 0
    for edge in list_edges:
        edges_copy = edges.copy()
        if checkCycles(edges_copy, edge) == False:
            long_run += list_edges_weight[edge]
            edges.append(edge)
        # if len(edges) == numNode-1:
        #     break
    return (long_run, edges)


if __name__ == "__main__":
    G = nx.Graph()
    G.add_weighted_edges_from(
        [
            ("A", "B", 3),
            ("A", "C", 1),
            ("B", "C", 7),
            ("B", "D", 5),
            ("B", "E", 1),
            ("C", "D", 2),
            ("D", "E", 7),
            ("E", "F", 2),
            ("D", "F", 3),
            ("C", "F", 1),
            ("C", "G", 3),
            ("A", "H", 3),
            ("C", "H", 3),
            ("A", "G", 2),
        ]
    )
    list_node = list(G.nodes)
    list_edges = list(G.edges)
    list_edges_weight = dict.fromkeys(list_edges)
    for edge in list_edges:
        list_edges_weight[edge] = G.get_edge_data(edge[0], edge[1])['weight']

    print(list_edges_weight)
    list_edges.sort(key=lambda x: list_edges_weight[x])
    start = time.time()
    print(Kruskal(list_edges, list_edges_weight, len(list_node)))
    end = time.time()
    print(f"Running time: { end-start} second")
