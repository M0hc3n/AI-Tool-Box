import heapq


import networkx as nx


class CustomGraph:

    """_summary_

    Returns:
        _dict_: returns the grph dict representation of a given graph_
    """
    __graph = {"A": [["B", 2], ["C", 3], 12],  # h(n) to G ,h(n) to F
               "B": [["A", 2], ["C", 4], ["D", 5], 10],
               "C": [["A", 3], ["B", 4], ["D", 3], ["F", 6], 8],
               "D": [["B", 5], ["C", 3], ["E", 2], 6],
               "E": [["G", 5], ["F", 3], ["D", 2], 4],
               "F": [["C", 6], ["E", 3], 6],
               "G": [["E", 5], 0]
               }

    @staticmethod
    def get_graph_dict():
        return CustomGraph.__graph

    """_summary_
    Returns:
        _nx_graph:The networkx Graph implmentation of the given dictionary
    """
    @staticmethod
    def get_nx_graph():
        G = nx.Graph()
        G.add_nodes_from(CustomGraph.__graph.keys())
        for k, v in CustomGraph.__graph.items():
            G.add_edges_from([(k, v[t][0]) for t in range(len(v)-2)])
        return G


class Node:

    """
    state:is the state object 
    cost:is the real cost of the node starting from the initial state state 
    score:is the  score of the node depending on the algorithm
    parent:is the parent node 
    action:action taken from parent to reach that node(from the set of legal actions)
    """

    def __init__(self, state, cost, score, parent, action):
        self.state = state
        self.cost = cost
        self.score = score
        self.parent = parent
        self.action = action
    def __str__(self):
        return self.state

    def __lt__(self, other):

        return self.score < other.score

    def __eq__(self, other):
        return self.state == other.state


class A_star:
    """
      initial_node: the initial node of the problem
      goal_state:the goal state of the problem
      problem:the graph representation of  the problem
    """

    def __init__(self, initial_state, goal_state, problem):
        self.problem = problem
        self.initial_node = Node(
            initial_state, 0, score=self.problem[initial_state][-1], parent=None, action=None)
        self.goal_state = goal_state

    def get_node_score(self, node, frontier):
        for element in frontier:
            if (node == element):
                return element.score

    def search(self):

        # back_tracking_set=[]
        frontier = []
        heapq.heappush(frontier, self.initial_node)
        explored = []

        while (True):
            if (len(frontier) == 0):
                return None

            current_node = heapq.heappop(frontier)
            explored.append(current_node)
            if (current_node.state == self.goal_state):
                # we return the whole explored set
                return explored

            for v in self.problem[current_node.state]:
                # generating the children
                if (not isinstance(v, int)):
                    cost = current_node.cost+v[1]
                    # f score
                    score = cost + self.problem[v[0]][-1]
                    child_node = Node(v[0], current_node.cost+v[1], score,
                                      parent=current_node, action=f"({current_node.state},{v[0]})")

                    heapq.heappush(frontier, child_node)
                    if (not (child_node in frontier) and not (child_node in explored)):
                        heapq.heappush(frontier, child_node)

                    elif (child_node in frontier and child_node.score < self.get_node_score(child_node, frontier)):
                        frontier.remove(child_node)
                        heapq.heappush(frontier, child_node)


algorithm = A_star("A", "G", CustomGraph.get_graph_dict())
for e in (algorithm.search()):
  print(e.parent)
