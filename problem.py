
class State:

    def __init__(self, label, neighbours=[]):
        self.label = label
        self.neighbours = neighbours

    def add_edge(state):
        # assuming undirected graph
        self.neighbours.append(state)
        state.add_edge(self)

class Problem:

    def __init__(self, states=[], start_state="", end_state=""):
        self.states = {}
        self.start_state = start_state
        self.end_state = end_state

    def __setattr__(self, name, value):
        self.states[name] = value

    def __getattribute__(self, name):
        return self.states[name]

    

    
