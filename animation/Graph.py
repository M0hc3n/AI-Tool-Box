import networkx as nx


class CustomGraph:

    """_summary_

    Returns:
        _dict_: returns the grph dict representation of a given graph_
    """
    __graph = {"A": [["B", 2], ["C", 3], 12],  # h(n) to G ,h(n) to F
               "B": [["A", 2], ["C", 4], ["D", 5], 15],
               "C": [["A", 3], ["B", 4], ["D", 3], ["F", 6], 13],
               "D": [["B", 5], ["C", 3], ["E", 2], 6],
               "E": [["G", 5], ["F", 3], ["D", 2], 4],
               "F": [["C", 6], ["E", 3], 6],
               "G": [["E", 5], 0]
               }

    @staticmethod
    def get_graph_dict():
        return CustomGraph.__graph

    """_summary_
    Returns:
        _nx_graph:The networkx Graph implmentation of the given dictionary
    """
    @staticmethod
    def get_nx_graph():
        G = nx.Graph()
        G.add_nodes_from(CustomGraph.__graph.keys())
        for k, v in CustomGraph.__graph.items():
            G.add_edges_from([(k, t[0], {
                "weight": t[1]}) for t in v if not isinstance(t, int)])
        return G

    @staticmethod
    def get_node_labeles_heuristic(problem):
        node_lables = []
        for k, v in CustomGraph.__graph.items():
            h = problem.min_heuristic_value(v)
            node_lables.append(f"{k}\n h={h}")
        return node_lables
