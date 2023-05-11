import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()
graph.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 4), (2, 5), (3, 6), (4, 7)])

pos = nx.spring_layout(graph, seed=42)

fig, ax = plt.subplots()

def update_dfs(path):
    node_colors = ['r' if i in path else 'b' for i in graph.nodes()]
    edge_colors = ['r' if (i, j) in zip(path, path[1:]) else 'b' for i, j in graph.edges()]
    ax.clear()
    nx.draw(graph,pos=pos , with_labels=True, node_color=node_colors, edge_color=edge_colors)
    plt.pause(1)  

start_node = 0
visited = set()
path = [start_node]

def dfs(node):
    visited.add(node)
    for neighbor in graph.neighbors(node):
        if neighbor not in visited:
            path.append(neighbor)
            update_dfs(path)
            dfs(neighbor)
            path.pop()

dfs(start_node)

# Display the final result
plt.show()
