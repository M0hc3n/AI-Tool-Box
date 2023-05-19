import heapq
from enum import Enum
from Node import Node
# this is an Enum for the variannts of the best first search techniques


class Variants(Enum):
    UCS = 1
    A_star = 2
    GREEDY = 3
    # we can add more similar algorithms


class Best_First_Search:
    """
      initial_node: the initial node of the problem
      goal_states:An array of goal states state to the problem
      problem:the graph representation of  the problem
    """

    def __init__(self, initial_state, goal_states, problem, algorithm=Variants.UCS):
        self.problem = problem
        self.initial_node = Node(
            initial_state, 0, score=self.problem[initial_state][-1], parent=None, action=None)
        self.goal_states = goal_states
        self.algorithm = algorithm

        """_summary_This is a function to return the min heuristic value among all
        list of the heuristics in case we have many goal nodes
        """

    def min_heuristic_value(self, value):
        min_value = float("inf")
        for v in value:
            if isinstance(v, int):
                min_value = min(min_value, v)

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

            current_node = heapq.heappop(frontier
                                         )
            explored.append(current_node)
            # here we stop when a goal is reached
            if (current_node.state in self.goal_states):
                # we return the whole explored set
                return explored

            for v in self.problem[current_node.state]:
                # generating the children
                if (not isinstance(v, int)):
                    # Node score depending on the type of the algorithm
                    if (self.algorithm == Variants.A_star):
                        cost = current_node.cost+v[1]
                        # here the heuristic value of a node is the min between all the heuristics
                        min_heuristic = self.min_heuristic_value(self.problem[current_node.state])
                        score = cost + self.problem[v[0]][-1]
                    elif (self.algorithm == Variants.UCS):
                        cost = current_node.cost+v[1]
                        score = cost
                    elif (self.algorithm == Variants.GREEDY):
                        score = self.min_heuristic_value(self.problem[current_node.state])
                    child_node = Node(v[0], current_node.cost+v[1], score,
                                      parent=current_node, action=f"({current_node.state},{v[0]})")

                    if (not (child_node in frontier) and not (child_node in explored)):
                        heapq.heappush(frontier, child_node)

                    elif (child_node in frontier and child_node.score < self.get_node_score(child_node, frontier)):
                        frontier.remove(child_node)
                        heapq.heappush(frontier, child_node)
