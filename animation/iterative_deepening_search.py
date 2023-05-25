from Node import Node
from utils import Variants
from depth_limited_search import DepthLimitedSearch


class IterativeDeepeningSearch:
    def __init__(self, initial_node, goal_states, problem, max_depth, step):
        self.initial_node = Node(
            initial_node, 0, score=0, parent=None, action=None, depth=0
        )
        self.goal_states = goal_states
        self.problem = problem
        self.explored = []
        self.max_depth = max_depth
        self.algorithm = Variants.IDS
        self.step = step

    def search(self):
        # Iterating while increasing the Depth until the Max Depth is reached.
        for depth in range(1, self.max_depth + 1, self.step):
            # Here we create an object of a depth limited search
            dls = DepthLimitedSearch(
                self.initial_node.state, self.goal_states, self.problem, limit=depth
            )
            self.explored.extend(dls.search())
            if dls.goal_found:
                return self.explored
        return self.explored
