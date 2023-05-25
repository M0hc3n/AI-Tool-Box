import networkx as nx


class CustomGraph:
    def __init__(self, graph):
        if (isinstance(graph, dict)):
            self.graph_dict = graph
            self.graph_nx = self.create_nx_graph(graph)

    def get_graph_dict(self):
        return self.graph_dict

    def get_nx_graph(self):
        return self.graph_nx

    def create_nx_graph(self, graph):
        G = nx.Graph()
        G.add_nodes_from(graph.keys())
        for k, v in graph.items():
            G.add_edges_from([
                (k, t[0], {"weight": t[1]})
                for t in v if  isinstance(t, list)])
        return G

    def add_edge(self, node_a_state, node_b_state, weight=1):

        if node_a_state not in self.graph_dict.keys():
            self.add_node(node_a_state)

        if node_b_state not in self.graph_dict.keys():
            self.add_node(node_b_state)
        self.graph_dict[node_a_state].insert(0, [node_b_state, weight])
        self.graph_dict[node_b_state].insert(0 , [node_a_state, weight])
        self.graph_nx = self.create_nx_graph(self.graph_dict)

    def add_node(self, state, heuristic=float("inf")):
        if (state not in self.graph_dict.keys()):
            self.graph_dict[state] = [heuristic]
        else:
            # since a  node can have multiple heuristics
            self.graph_dict[state].append(heuristic)
        self.graph_nx = self.create_nx_graph(self.graph_dict)

    def get_neighbors(self, state):
        arr = []
        for i in self.graph_dict[state]:
                if (type(i) == list):
                    arr.append(i[0])
        return arr

    @staticmethod
    def get_node_labeles_heuristic(problem):
        node_lables = []
        for k, v in problem.items():
            h = CustomGraph.min_heuristic_value(v)
            node_lables.append(f"{k}\n h={h}")
        return node_lables

    @staticmethod
    def min_heuristic_value(value):
        min_value = float("inf")
        for v in value:
            if not isinstance(v, list):
                min_value = min(min_value, v)
        return min_value
