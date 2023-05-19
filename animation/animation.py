import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Graph import CustomGraph
import time

class Animation:
    def __init__(self, algorithm):
        self.problem = algorithm
        self.graph = algorithm.problem

    def get_parent_path(self, path):

        currnet_node = path[-1]
        parent_path = [currnet_node]
        # we propaget from current state to parent
        while currnet_node.parent is not None:
            parent_path.append(currnet_node.parent)
            currnet_node = currnet_node.parent

        return [[node.parent.state if node.parent is not None else node.state,
                 node.state] for node in parent_path]

    def get_path_history(self):

        path = self.problem.search()

        # Generate animation frames
        path_history = []
        if path is not None:
            for i in range(len(path)):
                partial_path = path[:i+1]

                path_history.append(partial_path)

        return path_history

    def node_colors(self, path, unpacked_parent_path):
        return ['black' if node == self.problem.initial_node else 'yellow'
                if node.state in self.problem.goal_states
                else 'violet' if node == path[-1] else 'green'
                if (path[-1].state in self.problem.goal_states and node.state in unpacked_parent_path)else
                'blue' if node.state in unpacked_parent_path else 'red' for node in path]

    def update(self, num, path_history, ax, G, pos):
        ax.clear()
        graph_dict = self.graph.get_graph_dict()
        # Get the current path and path cost
        path = path_history[num]

        # drawing the base edges
        nx.draw_networkx_edges(G, pos=pos, edgelist=G.edges(),
                               ax=ax, edge_color="gray", width=6, alpha=0.5,  style="dashed")

        # Background nodes and edges(That is the nodes and edges that are not visited yet)
        null_nodes = nx.draw_networkx_nodes(
            G, pos=pos, nodelist=set(G.nodes()), node_color="black", ax=ax, node_size=1200)

        node_labels = CustomGraph.get_node_labeles_heuristic(
            problem=graph_dict)
        nx.draw_networkx_labels(G, pos=pos, labels=dict(zip(graph_dict.keys(), node_labels)),
                                font_color="white", ax=ax, font_size=10, font_family="sans-serif")
        null_nodes.set_edgecolor("black")

        # get the parent path so tha we can color the edges and nodes that are visited,not visted and the currently visited node
        parent_path = self.get_parent_path(path)
        unpacked_parent_path = [
            element for trace in parent_path for element in trace]

        query_nodes = nx.draw_networkx_nodes(
            G, pos=pos, nodelist=[node.state for node in path], node_color=self.node_colors(path, unpacked_parent_path),
            ax=ax, node_size=1200)
        query_nodes.set_edgecolor("white")

        edgelist = [[node.parent.state if node.parent is not None else node.state,
                     node.state] for node in path]

        # color any other path not from the parent node wtih the red color
        nx.draw_networkx_edges(G, pos=pos, edgelist=[v for v in edgelist if v not in parent_path],
                               edge_color="red", ax=ax, width=6, alpha=0.5,  style="dashed")

        # the yellow path from parent
        nx.draw_networkx_edges(G, pos=pos, edgelist=parent_path, width=6, alpha=0.5,  style="dashed",
                               edge_color=["green" if path[-1].state in self.problem.goal_states else "blue"], ax=ax)

        # drawing the costs
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels, font_size=10, font_family="sans-serif")
        time.sleep(1)


# here both graph and Algorithm are classes


    def animation_pop_up(self):
        G = self.graph.get_nx_graph()
        pos = nx.spring_layout(G)
        # perform the Search algorithm
        path_history = self.get_path_history()

        # creating the Tkinter Window
        root = tk.Tk()
        root.geometry("1920x1080")
        canvas = tk.Canvas(root)
        canvas.pack()

        # Create a Matplotlib figure and attach it to the canvas
        fig, ax = plt.subplots(figsize=(20, 20))
        fig_agg = FigureCanvasTkAgg(fig, master=canvas)
        fig_agg.get_tk_widget().pack()

        animate = animation.FuncAnimation(fig, self.update, frames=len(
            path_history), fargs=(path_history, ax, G, pos), interval=1000, repeat=True)
        root.mainloop()

