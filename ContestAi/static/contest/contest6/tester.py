import networkx as nx
import time


def searchFrontier(inGraph, node):
    nei = list(G.neighbors(node))
    frontier = []
    for i in nei:
        if i in inGraph:
            nei.remove(i)
        else:
            frontier.append((node, i, G.get_edge_data(node, i)['weight']))
    return frontier


def Prims(list_node):
    inGraph = ['H']
    edgeInGraph = []
    search = []
    frontier = []
    while len(inGraph) < len(list_node):
        search.append(inGraph[-1])
        frontier.extend((searchFrontier(inGraph, search.pop(0))))
        frontier.sort(key=lambda x: x[2])
        try:
            edge = frontier.pop(0)
            edgeInGraph.append(edge)
            inGraph.append(edge[1])
        except:
            continue
    return edgeInGraph


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
    start = time.time()

    print(Prims(list_node))
    end = time.time()
    print(f"Running time: { end-start} second")
