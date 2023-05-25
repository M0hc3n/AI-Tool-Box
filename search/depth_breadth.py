from Node import Node
from utils import Variants


class DepthBreadthFirstSearch:
  

    def __init__(self, initial_node, goal_states, problem, algorithm=Variants.DFS):

        self.initial_node = Node(
            initial_node, 0, score=0 , parent=None, action=None)
        self.goal_states = goal_states
        self.problem = problem
        self.explored = []  
        self.algorithm = algorithm
        if self.algorithm == Variants.DFS:
            self.index = -1
        elif self.algorithm == Variants.BFS:
            self.index = 0

    def search(self):

        stack = [self.initial_node]  

        while stack:
            current_node = stack.pop(self.index)  

            if current_node in self.explored:
                continue

            self.explored.append(current_node)

            if current_node.state in self.goal_states:
                return self.explored

            for v in self.problem.graph_dict[current_node.state]:
                if isinstance(v, list):
                    new_node = Node(v[0], current_node.cost+v[1], 0, current_node, None)
                    if new_node not in self.explored:
                        stack.append(new_node)
        return self.explored 
