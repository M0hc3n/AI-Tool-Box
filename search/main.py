import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def add_node():
    node_name = node_name_entry.get()
    node_value = node_value_entry.get()


    graph.add_node(node_name, value=node_value)

    print("Added node:", node_name, node_value)

def add_edge():
    source_node = source_node_entry.get()
    target_node = target_node_entry.get()
    path_cost = path_cost_entry.get() 

    
    graph.add_edge(source_node, target_node, weight=path_cost)

    print("Added edge:", source_node, "->", target_node)

def create_graph():

    print("Graph created!")

    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)


    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title("Graph Entry")

root.geometry("300x300")

graph = nx.Graph()

node_name_label = tk.Label(root, text="Node Name:")
node_name_label.pack()
node_name_entry = tk.Entry(root)
node_name_entry.pack()

node_value_label = tk.Label(root, text="Node Value:")
node_value_label.pack()
node_value_entry = tk.Entry(root)
node_value_entry.pack()

add_node_button = tk.Button(root, text="Add Node", command=add_node)
add_node_button.pack()

source_node_label = tk.Label(root, text="Source Node:")
source_node_label.pack()
source_node_entry = tk.Entry(root)
source_node_entry.pack()

target_node_label = tk.Label(root, text="Target Node:")
target_node_label.pack()
target_node_entry = tk.Entry(root)
target_node_entry.pack()

path_cost_label = tk.Label(root, text="Path Cost:")
path_cost_label.pack()
path_cost_entry = tk.Entry(root)
path_cost_entry.pack()


add_edge_button = tk.Button(root, text="Add Edge", command=add_edge)
add_edge_button.pack()


create_graph_button = tk.Button(root, text="Create Graph", command=create_graph)
create_graph_button.pack()


root.mainloop()
