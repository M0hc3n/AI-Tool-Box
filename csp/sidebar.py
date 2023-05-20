import tkinter as tk
import networkx as nx
from MapColor import MapColor

class SideBar(tk.Frame):

    def __init__(self, parent):

        super().__init__(parent)

        self.parent = parent

        self.node_name_label = tk.Label(self, text="State Name:")
        self.node_name_label.grid(column=0, row=0)
        self.node_name_entry = tk.Entry(self)
        self.node_name_entry.grid(column=1, row=0)

        self.add_node_button = tk.Button(
            self, text="Add Node", command=self.add_node)
        self.add_node_button.grid(column=0, row=2, columnspan=2, sticky="nsew")

        self.source_node_label = tk.Label(self, text="Source State:")
        self.source_node_label.grid(column=0, row=3)
        self.source_node_entry = tk.Entry(self)
        self.source_node_entry.grid(column=1, row=3)

        self.target_node_label = tk.Label(self, text="Target State:")
        self.target_node_label.grid(column=0, row=4)
        self.target_node_entry = tk.Entry(self)
        self.target_node_entry.grid(column=1, row=4)

        self.add_edge_button = tk.Button(
            self, text="Add Edge", command=self.add_edge)
        self.add_edge_button.grid(column=0, row=9, columnspan=2, sticky="nsew")

        self.number_of_colors_label = tk.Label(self, text="Number of Colors:")
        self.number_of_colors_label.grid(column=0, row=10)
        self.number_of_colors_entry = tk.Entry(self)
        self.number_of_colors_entry.grid(column=1, row=10)


        self.apply_algorithm_button = tk.Button(
            self, text="Apply Search Algorithm", command=self.solve_csp)
        self.apply_algorithm_button.grid(column=0, row=11, columnspan=2, sticky="nsew")

    def add_node(self):
        node_name = self.node_name_entry.get()

        if node_name not in self.parent.graph:
            self.parent.graph.add_node(node_name)
            print("Added node:", node_name)

        self.parent._update_graph()

    def add_edge(self):
        source_node = self.source_node_entry.get()
        target_node = self.target_node_entry.get()

        self.parent.graph.add_edge(source_node, target_node)
        print("Added edge:", source_node, "->", target_node)

        self.parent._update_graph()

    def convert_top_map_graph(self):
        map_graph = {}

        for key, value in nx.to_dict_of_dicts(self.parent.graph).items():
            inner_keys = set(value.keys())
            map_graph[key] = inner_keys

        return map_graph

    def solve_csp(self):
        print(
            nx.to_dict_of_dicts(self.parent.graph)
        )

        map_graph = self.convert_top_map_graph()

        map_coloring_problem = MapColor(map_graph)

        map_coloring_problem.solve_problem({'r','b','y','g'})

