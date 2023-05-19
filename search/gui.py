import tkinter as tk
import networkx as nx
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



matplotlib.use("tkagg")

class Window(tk.Tk):

    def __init__(self, title_="Graph Entry", geometry_="300x300"):
 
        super().__init__()

        self.title(title_)

        self.geometry(geometry_)

        self.graph = nx.Graph()


        self.node_name_label = tk.Label(self, text="Node Name:")
        self.node_name_label.pack()
        self.node_name_entry = tk.Entry(self)
        self.node_name_entry.pack()

        self.node_value_label = tk.Label(self, text="Node Value:")
        self.node_value_label.pack()
        self.node_value_entry = tk.Entry(self)
        self.node_value_entry.pack()

        self.add_node_button = tk.Button(self, text="Add Node", command=self.add_node)
        self.add_node_button.pack()

        self.source_node_label = tk.Label(self, text="Source Node:")
        self.source_node_label.pack()
        self.source_node_entry = tk.Entry(self)
        self.source_node_entry.pack()

        self.target_node_label = tk.Label(self, text="Target Node:")
        self.target_node_label.pack()
        self.target_node_entry = tk.Entry(self)
        self.target_node_entry.pack()

        self.path_cost_label = tk.Label(self, text="Path Cost:")
        self.path_cost_label.pack()
        self.path_cost_entry = tk.Entry(self)
        self.path_cost_entry.pack()

        self.add_edge_button = tk.Button(
            self, text="Add Edge", command=self.add_edge)
        self.add_edge_button.pack()

        self.create_graph_button = tk.Button(
            self, text="Create Graph", command=self.create_graph)
        self.create_graph_button.pack()

        self.add_drop_down_menu()

        self.apply_algorithm_button = tk.Button(
            self, text="Apply Search Algorithm", command=self.apply_algorithm)
        self.apply_algorithm_button.pack()


    def add_node(self):
        node_name = self.node_name_entry.get()
        node_value = self.node_value_entry.get()

        self.graph.add_node(node_name, value=node_value)

        print("Added node:", node_name, node_value)

    def add_edge(self):
        source_node = self.source_node_entry.get()
        target_node = self.target_node_entry.get()
        path_cost = self.path_cost_entry.get()

        self.graph.add_edge(source_node, target_node, weight=path_cost)

        print("Added edge:", source_node, "->", target_node)

    def create_graph(self):
        import matplotlib.pyplot as plt
        print("Graph created!")

        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True,
                node_color='lightblue', node_size=500, font_size=10)

        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)

        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def add_drop_down_menu(self):
        options = [
            "Breadth First Search",
            "Depth First Search",
            "Uniform Cost Search",
            "Depth Limited",
            "Iterative Deepening Search",
            "Greedy Best First Search",
            "A* Star"
        ]

        clicked = tk.StringVar()

        clicked.set("Breadth First Search")


        drop = tk.OptionMenu(self, clicked, *options)
        drop.pack()

    def apply_algorithm(self):
        print('applying the algorithm')

