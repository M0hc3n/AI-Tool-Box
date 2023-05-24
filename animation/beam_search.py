import heapq
from Node import Node
from Graph import CustomGraph
from utils import Variants


class BeamSearch:
  

    def __init__(self, initial_node, goal_states, problem, algorithm=Variants.BEAM,width=2):

        self.initial_node = Node(
            initial_node, 0, score=0 , parent=None, action=None)
        self.goal_states = goal_states
        self.problem = problem
        self.explored = []  
        self.algorithm = algorithm
        self.beam_width = width

    def get_node_score(self, node, frontier):
        for element in frontier:
            if (node == element):
                return element.score

    def generate_node(self, current_node, v):
        cost = current_node.cost+v[1]
        # here the heuristic value of a node is the min between all the heuristics
        min_heuristic = CustomGraph.min_heuristic_value(
            self.problem.graph_dict[v[0]])
        score = min_heuristic
        return Node(v[0], current_node.cost+v[1], score,
                    parent=current_node, action=f"({current_node.state},{v[0]})")
    
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

            for v in self.problem.graph_dict[current_node.state]:
                # generating the children
                if (isinstance(v, list)):
                    # generate a child
                    child_node = self.generate_node(current_node, v)
                    if (not (child_node in frontier) and not (child_node in explored)):
                        heapq.heappush(frontier, child_node)

                    elif (child_node in frontier and child_node.score < self.get_node_score(child_node, frontier)):
                        frontier.remove(child_node)
                        heapq.heappush(frontier, child_node)
            counter=0
            oldopen = frontier
            frontier = []
            while(counter <= self.beam_width):
                node = heapq.heappop(oldopen)
                heapq.heappush(frontier, node)
                counter += 1