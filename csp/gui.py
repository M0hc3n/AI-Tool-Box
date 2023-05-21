import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from sidebar import SideBar


class Window(tk.Tk):

    def __init__(self, title="Graph Entry", geometry="700x700"):

        super().__init__()

        self.title(title)

        self.geometry(geometry)

        self.graph = nx.Graph()

        self.nodes_with_colors = {}

        self.sidebar = SideBar(self)
        self.sidebar.pack(side="left", fill="y", ipadx=30, ipady=10)

        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self)
        self.canvas.get_tk_widget().pack(fill="both")


    def _clear(self):
        for item in self.canvas.get_tk_widget().find_all():
            self.canvas.get_tk_widget().delete(item)

    def _update_graph(self):
        plt.clf()

        pos = nx.spring_layout(self.graph)
        

        if(len( self.nodes_with_colors.keys() ) > 0):
            nx.draw(self.graph, pos, with_labels=True, node_color=[self.nodes_with_colors[node] for node in self.graph.nodes() ], node_size=800, font_size=10 )
        else:
            nx.draw(self.graph, pos, with_labels=True,
                node_color='lightblue', node_size=800, font_size=10)

        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

        self.canvas.draw()
