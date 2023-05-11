import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import networkx as nx
import random
from Graph import CustomGraph


# Graph Creation
G = CustomGraph.get_nx_graph()
graph_dict = CustomGraph.get_graph_dict()

# This is a method to get the canvas position of the implemented graph of each node
pos = nx.spring_layout(G)

# Build plot
fig, ax = plt.subplots(figsize=(20, 20))

path = ["A"]

def breadthFirstTraversal(Graph, start): 
    visited = {}
    queue = [start]
    path = [start]

    for node in Graph:
        visited[node] = False
    
    while len(queue) > 0:
        curr = queue.pop(0)

        if( visited[curr] == False ):
            visited[curr] = True
            path.append(curr)

            
            for child in Graph[curr]:
                queue.append(child)


def update(num):
    ax.clear()


    path.append(chr(ord(path[ len(path) - 1 ]) + 1 ))


    # Background nodes
    nx.draw_networkx_edges(G, pos=pos, ax=ax, edge_color="gray")
    null_nodes = nx.draw_networkx_nodes(G, pos=pos, nodelist=set(
        G.nodes()) - set(path), node_color="white",  ax=ax)
    null_nodes.set_edgecolor("black")

    # Query nodes
    query_nodes = nx.draw_networkx_nodes(
        G, pos=pos, nodelist=path, node_color='red', ax=ax)

    query_nodes.set_edgecolor("white")
    nx.draw_networkx_labels(G, pos=pos, labels=dict(
        zip(path, path)),  font_color="white", ax=ax)
    edgelist = [path[k:k+2] for k in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos=pos, edgelist=edgelist,
                          ax=ax)

    # Scale plot ax
    ax.set_title("Frame %d:    " % (num+1) +
                 " - ".join(path), fontweight="bold")
    ax.set_xticks([])
    ax.set_yticks([])


# Create a Tkinter window
root = tk.Tk()
root.geometry("800x600")

# Create a Tkinter canvas
canvas = tk.Canvas(root)
canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create a Matplotlib figure and attach it to the canvas
fig_agg = FigureCanvasTkAgg(fig, master=canvas)
fig_agg.draw()
fig_agg.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create the animation object
ani = animation.FuncAnimation(fig, update, frames=None, interval=1000, repeat=True)

# Start the animation
ani.event_source.start()

# Start the Tkinter event loop
root.mainloop()