import webcolors


class MapColor:

    def __init__(self, graph, num_of_colors):
        self.graph = graph

        self.generate_colors(num_of_colors)

        print(self.graph)

    # generate a set of colors based on the given number
    def generate_colors(self,num_colors):
        all_colors = webcolors.CSS3_NAMES_TO_HEX
        color_names = list(all_colors.keys())[:num_colors]
        self.set_of_colors = set(color_names)


    def check_valid(self):
        for node,nexts in self.graph.items():
            # check that the format of graph is valid
            assert(node not in nexts) 
            for next in nexts:
                # check that if A has B as a neighbor, then B has as a neighbor
                assert(next in self.graph and node in self.graph[next]) 

    def check_solution(self, solution):
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

    def find_best_candidate(self, guesses):

        # we use -1 * each metric so that, when sorting, we favourite the neighbor
        # with the most number of colored neighbors (i.e: least number of possible colors)
        # in case of a tie, we will favourite the second element of the tuple
        # which stands for the number of possible colors, (the most you have, the favourite you are to be chosen as a second option)  
        candidates_with_add_info = [
            (
            # this gets the number of colored neighbors == number of forbidden colors
            -len({guesses[neigh] for neigh in self.graph[n] if neigh     in guesses}), 
            # this gets the number uncolored neighbors == number of possible colors
            -len({neigh          for neigh in self.graph[n] if neigh not in guesses}), # minus nb_uncolored_neighbour
            n
            ) for n in self.graph if n not in guesses]
        print(candidates_with_add_info)
        candidates_with_add_info.sort()
        print(candidates_with_add_info)
        candidates = [n for _,_,n in candidates_with_add_info]
    
        if candidates:
            candidate = candidates[0]
            assert(candidate not in guesses)
            return candidate

        assert(set(self.graph.keys()) == set(guesses.keys()))
        return None


    def solve(self, guesses, depth):
        n = self.find_best_candidate( guesses)

        # basecase, in case no best candidates remaining to be assigned
        if n is None:
            return guesses

        for c in self.set_of_colors - {guesses[neigh] for neigh in self.graph[n] if neigh in guesses}:
            assert(n not in guesses)
            assert(all((neigh not in guesses or guesses[neigh] != c) for neigh in self.graph[n]))
            guesses[n] = c
            indent = '  '*depth
            print ("%sTrying to give color %s to %s" % (indent,c,n))

            if self.solve( guesses, depth+1):
                print ("%sGave color %s to %s" % (indent,c,n))
                return guesses

            else:
                del guesses[n]
                print ("%sCannot give color %s to %s" % (indent,c,n))

        return None

    def solve_problem(self):
        self.check_valid()
        solution = self.solve( guesses=dict(), depth=0)
        
        print(solution)
        if( not self.check_solution(solution) ):
            return False

        return solution
