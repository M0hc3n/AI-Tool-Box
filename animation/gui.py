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

        self.graph = nx.Graph()
        self.custom_graph = CustomGraph(graph = {})

        self.sidebar = SideBar(self)
        self.sidebar.pack(side="left", fill="y")

        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self)
        self.canvas.get_tk_widget().pack(fill="both")

    def _clear(self):
        for item in self.canvas.get_tk_widget().find_all():
            self.canvas.get_tk_widget().delete(item)

    def _update_graph(self):
        plt.clf()

        pos = nx.spring_layout(self.graph)
        nx.draw_networkx_edges(self.graph, pos=pos, edgelist=self.graph.edges(),
                                edge_color="gray", width=6, alpha=0.5,  style="dashed")

        null_nodes = nx.draw_networkx_nodes(
            self.graph, pos=pos, nodelist=set(self.graph.nodes()), node_color="black",  node_size=1200)

        node_labels = CustomGraph.get_node_labeles_heuristic(
            problem=self.custom_graph.graph_dict)
        nx.draw_networkx_labels(self.graph, pos=pos, labels=dict(zip(self.custom_graph.graph_dict.keys(), node_labels)),
                                font_color="white",  font_size=10, font_family="sans-serif")

        # drawing the costs
        edge_labels = nx.get_edge_attributes(self.graph, "weight")
        nx.draw_networkx_edge_labels(
            self.graph, pos, edge_labels, font_size=15, font_family="sans-serif")

        null_nodes.set_edgecolor("black")

        self.canvas.draw()

        