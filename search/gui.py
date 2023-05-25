import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from sidebar import SideBar
from Graph import CustomGraph


class Window(tk.Tk):

    def __init__(self, title="Graph Entry", geometry="300x300"):

        super().__init__()

        self.title(title)

        self.geometry(geometry)
        self.fig, self.ax = plt.subplots(figsize=(15, 20))

        self.graph = nx.Graph()
        self.custom_graph = CustomGraph(graph={})

        self.sidebar = SideBar(self)
        self.sidebar.pack(side="left", fill="y")

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill="both")
        
        self.goal_states = []
        self.initial_state = ''

    def _clear(self):
        for item in self.canvas.get_tk_widget().find_all():
            self.canvas.get_tk_widget().delete(item)

    def _update_graph(self):
        self.ax.clear()
        pos = nx.spring_layout(self.graph)
        nx.draw_networkx_edges(self.graph, pos=pos, ax=self.ax, edgelist=self.graph.edges(),
                               edge_color="gray", width=6, alpha=0.5,  style="dashed")
        print(self.graph.nodes())
        null_nodes = nx.draw_networkx_nodes(
            self.graph, pos=pos, ax=self.ax, nodelist=set(self.graph.nodes()) - set(self.goal_states) - set(self.initial_state), node_color="black",  node_size=1200)

        green_nodes = nx.draw_networkx_nodes(
            self.graph, pos=pos, ax=self.ax, nodelist=set(self.goal_states) - set(self.initial_state), node_color="green",  node_size=1200)

        initial_node = nx.draw_networkx_nodes(
            self.graph, pos=pos, ax=self.ax, nodelist=set(self.initial_state), node_color="orange",  node_size=1200)

        node_labels = CustomGraph.get_node_labeles_heuristic(
            problem=self.custom_graph.graph_dict)
        nx.draw_networkx_labels(self.graph, pos=pos, ax=self.ax, labels=dict(zip(self.custom_graph.graph_dict.keys(), node_labels)),
                                font_color="white",  font_size=10, font_family="sans-serif")

        # drawing the costs
        edge_labels = nx.get_edge_attributes(self.graph, "weight")
        nx.draw_networkx_edge_labels(
            self.graph, pos, edge_labels, font_size=15, font_family="sans-serif")

        null_nodes.set_edgecolor("black")
        green_nodes.set_edgecolor("green")
        initial_node.set_edgecolor("orange")

        # self._clear()
        self.canvas.draw()
