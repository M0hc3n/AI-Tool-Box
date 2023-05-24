from Node import Node
from utils import Variants


class DepthLimitedSearch:

    def __init__(self, initial_node, goal_states, problem, limit):

        self.initial_node = Node(
            initial_node, 0, score=0, parent=None, action=None, depth=0)
        self.goal_states = goal_states
        self.problem = problem
        self.explored = []
        self.limit = limit
        self.algorithm = Variants.DPL

    def search(self):

        stack = [self.initial_node]

        while stack:
            current_node = stack.pop()

            if current_node in self.explored:
                continue

            self.explored.append(current_node)

            if current_node.state in self.goal_states:
                return self.explored

            for v in self.problem.graph_dict[current_node.state]:
                if isinstance(v, list):
                    new_node = Node(v[0], current_node.cost+v[1], 0, current_node,
                                    None, current_node.depth+1)
                    if new_node not in self.explored and new_node.depth <= self.limit:
                        stack.append(new_node)
        return self.explored
