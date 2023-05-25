import webcolors


class MapColor:

    def __init__(self, graph, num_of_colors):
        self.graph = graph

        self.generate_colors(num_of_colors)

    # generate a set of colors based on the given number
    def generate_colors(self,num_colors):
        all_colors = webcolors.CSS3_NAMES_TO_HEX
        color_names = list(all_colors.keys())[:num_colors]
        self.set_of_colors = set(color_names)


    def is_valid_graph(self):
        for node,nexts in self.graph.items():
            # check that the format of graph is valid
            assert(node not in nexts) 
            for next in nexts:
                # check that if A has B as a neighbbor, then B has as a neighbor
                assert(next in self.graph and node in self.graph[next]) 

    def is_valid_solution(self, solution):
        if solution is not None:
            for node,nexts in self.graph.items():
                assert(node in solution)
                color = solution[node]
                # make sure that for any node, its neighbors are colored differently
                for next in nexts:
                    assert(next in solution and solution[next] != color)
            return True
        else: 
            return False


    # the logic of this function was inspired by: 
    # https://codereview.stackexchange.com/users/9452/sylvaind
    def find_best_candidate(self, assignments):

        # we use -1 * each metric so that, when sorting, we favourite the neighbor
        # with the most number of colored neighbors (i.e: least number of possible colors)
        # in case of a tie, we will favourite the second element of the tuple
        # which stands for the number of possible colors, (the most you have, the favourite you are to be chosen as a second option)  
        all_possible_candidates = [
            (
            # this gets the number of colored neighbors == number of forbidden colors
            -len({assignments[neigh] for neigh in self.graph[node] if neigh     in assignments}), 
            # this gets the number uncolored neighbors == number of possible colors
            -len({neigh          for neigh in self.graph[node] if neigh not in assignments}), # minus nb_uncolored_neighbour
            node
            ) for node in self.graph if node not in assignments]
        all_possible_candidates.sort()
        candidates = [node for _,_,node in all_possible_candidates]
    
        if candidates:
            candidate = candidates[0]
            assert(candidate not in assignments)
            return candidate

        assert(set(self.graph.keys()) == set(assignments.keys()))
        return None


    def solve(self, assignments):
        state = self.find_best_candidate( assignments )

        # basecase, in case no best candidates remaining to be assigned
        if state is None:
            return assignments

        for color in self.set_of_colors - {assignments[neighbor] for neighbor in self.graph[state] if neighbor in assignments}:
            assert(state not in assignments)
            assert(all((neighbor not in assignments or assignments[neighbor] != color) for neighbor in self.graph[state]))
            assignments[state] = color

            if self.solve( assignments ):
                return assignments
            else:
                del assignments[state]

        return None

    def color_map(self):
        self.is_valid_graph()
        solution = self.solve( assignments=dict() )
        
        if( not self.is_valid_solution( solution ) ):
            return False

        return solution
