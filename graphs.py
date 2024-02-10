from permutation import Permutation
import networkx as nx
import matplotlib.pyplot as plt


def constructGraph(data: dict, G):
    for node, neighbors in data.items():
        G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    color_map = []
    for (node, val) in G.degree():
        color_map.append('green' if len([m for m in node if m % 2 == 0]) % 2 == 0 else 'orange')

    renaming_mapping = {}
    for node, data in G.nodes(data=True):
        renaming_mapping[node] = f'({node[0]})' if len(node) == 1 else str(node)

    new_gr = nx.relabel_nodes(G, renaming_mapping)

    nx.draw_spring(new_gr, node_size=500, with_labels=True, node_color=color_map, alpha=0.8)


def drawRootGraph(cardinality: int, degree: int = 2):
    data = {}
    for perm in Permutation.createEmbassyOfGroup(cardinality):
        data[perm.cycle_structure] = perm.getRootStructures(degree)

    G = nx.DiGraph()

    constructGraph(data, G)

    plt.title(f"Degree root extraction graph {degree} for group S{cardinality}", loc='center')
    plt.show()


def drawCommutativeGraph(cardinality: int):
    data = {}

    for perm in Permutation.createEmbassyOfGroup(cardinality)[1:]:
        data[perm.cycle_structure] = perm.getCommutativeStructures()

    G = nx.Graph()

    constructGraph(data, G)

    plt.title(f"The commutative graph of cyclic structures for the group S{cardinality}", loc='center')
    plt.show()


def drawStabilizingGraph(cardinality: int, leftMult=False):
    data = {}
    for perm in Permutation.createEmbassyOfGroup(cardinality)[1:]:
        data[perm.cycle_structure] = perm.getStabilizingStructures(leftMult=leftMult)

    G = nx.DiGraph()

    constructGraph(data, G)
    plt.title(f"Stabilizing graph for the group S_{cardinality}, left multiplication: {leftMult}", loc='center')
    plt.show()


if __name__ == '__main__':
    pass
