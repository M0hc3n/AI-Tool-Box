import tkinter as tk
import networkx as nx
import animation
import best_first_search
from Graph import CustomGraph

# Best_First_Search, Variants


class SideBar(tk.Frame):

    def __init__(self, parent):

        super().__init__(parent)

        self.parent = parent
        self.goalStates=[]

        self.node_name_label = tk.Label(self, text="Node Name:")
        self.node_name_label.grid(column=0, row=0)
        self.node_name_entry = tk.Entry(self)
        self.node_name_entry.grid(column=1, row=0)

        self.node_value_label = tk.Label(self, text="Node Value:")
        self.node_value_label.grid(column=0, row=1)
        self.node_value_entry = tk.Entry(self)
        self.node_value_entry.grid(column=1, row=1)

        self.add_node_button = tk.Button(
            self, text="Add Node", command=self.add_node)
        self.add_node_button.grid(column=0, row=2, columnspan=2, sticky="nsew")

        self.source_node_label = tk.Label(self, text="Source Node:")
        self.source_node_label.grid(column=0, row=3)
        self.source_node_entry = tk.Entry(self)
        self.source_node_entry.grid(column=1, row=3)

        self.target_node_label = tk.Label(self, text="Target Node:")
        self.target_node_label.grid(column=0, row=4)
        self.target_node_entry = tk.Entry(self)
        self.target_node_entry.grid(column=1, row=4)
        

        self.path_cost_label = tk.Label(self, text="Path Cost:")
        self.path_cost_label.grid(column=0, row=5)
        self.path_cost_entry = tk.Entry(self)
        self.path_cost_entry.grid(column=1, row=5)

        self.add_edge_button = tk.Button(
            self, text="Add Edge", command=self.add_edge)
        self.add_edge_button.grid(column=0, row=9, columnspan=2, sticky="nsew")

        self.add_drop_down_menu()

        self.apply_algorithm_button = tk.Button(
            self, text="Apply Search Algorithm", command=self.apply_algorithm)

            
        self.initial_node_label = tk.Label(self, text="Initial Node:")
        self.initial_node_label.grid(column=0, row= 10)
        self.initial_node_entry = tk.Entry(self)
        self.initial_node_entry.grid(column=1, row= 10)

        self.goal_node_label = tk.Label(self, text="Goal Node:")
        self.goal_node_label.grid(column=0, row=11)
        self.goal_node_entry = tk.Entry(self)
        self.goal_node_entry.grid(column=1, row=11)

        self.apply_algorithm_button.grid(
            column=0, row=13, columnspan=2, sticky="nsew")

    def add_node(self):
        node_name = self.node_name_entry.get()
        node_value = int(self.node_value_entry.get())

        self.parent.graph.add_node(node_name, value=node_value)
        self.parent.custom_graph.add_node(node_name, node_value)

        print("Added node:", node_name, node_value)

        self.parent._update_graph()

    def add_edge(self):
        source_node = self.source_node_entry.get()
        target_node = self.target_node_entry.get()
        path_cost = int(self.path_cost_entry.get())

        self.parent.graph.add_edge(source_node, target_node, weight=path_cost)
        self.parent.custom_graph.add_edge(
            source_node, target_node, weight=path_cost)
        print("Added edge:", source_node, "->", target_node)

        self.parent._update_graph()

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
        drop.grid(column=0, row=12, sticky="nsew", columnspan=2)

    def apply_algorithm(self):
        print(nx.spring_layout(self.parent.custom_graph.graph_nx))
        algo = best_first_search.Best_First_Search(
            self.initial_node_entry.get(), ["G"], problem=self.parent.custom_graph, algorithm=best_first_search.Variants.UCS)
        animate = animation.Animation(algo)
        animate.animation_pop_up()
