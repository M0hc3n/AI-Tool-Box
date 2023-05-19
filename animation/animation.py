import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Graph import CustomGraph
from best_first_search import Best_First_Search
from best_first_search import Variants
# Graph Creation



# here both graph and Algorithm are classes
def animation_pop_up(graph,Algorithm):
        
    graph_dict = graph.get_graph_dict()
    problem = Algorithm(
        "A", goal_states=["G"], problem=graph_dict, algorithm=Variants.UCS)
    G = CustomGraph.get_nx_graph()
    pos = nx.spring_layout(G)

    # Build plot
    fig, ax = plt.subplots(figsize=(20, 20))
    
    
    def get_parent_path(path):
        
        currnet_node = path[-1]
        parent_path = [
            currnet_node
        ]
        # we propaget from current state to parent 
        while currnet_node.parent is not None:
            parent_path.append(currnet_node.parent)
            currnet_node = currnet_node.parent


        return [[node.parent.state if node.parent is not None else node.state,
                       node.state] for node in parent_path]



    def update(num, path_history):


        ax.clear()
        # Get the current path and path cost
        path = path_history[num]

        # drawing the
        nx.draw_networkx_edges(G, pos=pos, edgelist=G.edges(),
                               ax=ax, edge_color="gray")
        # Background nodes and edges(That is the nodes and edges that are not visited yet)

        null_nodes = nx.draw_networkx_nodes(
            G, pos=pos, nodelist=set(G.nodes()), node_color="black", ax=ax)

        nx.draw_networkx_labels(G, pos=pos, labels=dict(zip(graph_dict.keys(), graph_dict.keys())),
                                font_color="white", ax=ax)
        null_nodes.set_edgecolor("black")

        # get the parent path so tha we can color the edges and nodes that are visited,not visted and the currently visited node
      
        parent_path=get_parent_path(path)
     
        query_nodes = nx.draw_networkx_nodes(
            G, pos=pos, nodelist=[node.state for node in path], node_color=['black' if node==problem.initial_node else 'violet' if node==path[-1] else 'green' if  path[-1].state in problem.goal_states else  'blue' if node.state in [element  for trace in parent_path for element in trace] else 'red' for node in path], ax=ax)
        query_nodes.set_edgecolor("white")
        # Query nodes
        nx.draw_networkx_labels(G, pos=pos, labels=dict(zip([node.state for node in path], [node.state for node in path])),
                                font_color="white", ax=ax)
        edgelist = [[node.parent.state if node.parent is not None else node.state,
                     node.state] for node in path]



        # color any other path not from the parent node wtih the red color
        nx.draw_networkx_edges(G, pos=pos, edgelist=[v for v in edgelist if v not in parent_path],
                               edge_color="red", ax=ax)


        # the yellow path from parent
        nx.draw_networkx_edges(G, pos=pos, edgelist=parent_path,
                               edge_color=["green" if  path[-1].state in problem.goal_states else "blue"], ax=ax)

        ax.set_xticks([])
        ax.set_yticks([])
        plt.pause(1)


    # Run the A* search algorithm

    path = problem.search()

    # Generate animation frames
    path_history = []
    if path is not None:
        for i in range(len(path)):
            partial_path = path[:i+1]

            path_history.append(partial_path)

    # Create the animation object


    root = tk.Tk()
    root.geometry("800x600")

    # Create a Tkinter canvas
    canvas = tk.Canvas(root)
    canvas.pack()

    # Create a Matplotlib figure and attach it to the canvas
    fig_agg = FigureCanvasTkAgg(fig, master=canvas)
    # fig_agg.draw()
    fig_agg.get_tk_widget().pack()

    # Create the animation object
    ani = animation.FuncAnimation(fig, update, frames=len(
        path_history), fargs=(path_history,), interval=1000, repeat=True)

    # Start the animation
    ani.event_source.start()

    # Start the Tkinter event loop
    root.mainloop()

animation_pop_up(CustomGraph,Best_First_Search)