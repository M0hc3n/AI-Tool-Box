import webcolors


class MapColor:

    def __init__(self, graph, num_of_colors):
        self.graph = graph

        self.generate_colors(num_of_colors)

        print(self.graph)

    def generate_colors(self,num_colors):
        all_colors = webcolors.CSS3_NAMES_TO_HEX
        color_names = list(all_colors.keys())[:num_colors]
        self.set_of_colors = set(color_names)


    def check_valid(self):
        for node,nexts in self.graph.items():
            assert(node not in nexts) # no node linked to itself
            for next in nexts:
                assert(next in self.graph and node in self.graph[next]) # A linked to B implies B linked to A

    def check_solution(self, solution):
        if solution is not None:
            for node,nexts in self.graph.items():
                assert(node in solution)
                color = solution[node]
                for next in nexts:
                    assert(next in solution and solution[next] != color)
            return True
        else: 
            return False

    def find_best_candidate(self, guesses):

        candidates_with_add_info = [
            (
            -len({guesses[neigh] for neigh in self.graph[n] if neigh     in guesses}), # nb_forbidden_colors
            -len({neigh          for neigh in self.graph[n] if neigh not in guesses}), # minus nb_uncolored_neighbour
            n
            ) for n in self.graph if n not in guesses]
        candidates_with_add_info.sort()
        candidates = [n for _,_,n in candidates_with_add_info]
    
        if candidates:
            candidate = candidates[0]
            assert(candidate not in guesses)
            return candidate

        assert(set(self.graph.keys()) == set(guesses.keys()))
        return None


    def solve(self, guesses, depth):
        n = self.find_best_candidate( guesses)

        if n is None:
            return guesses # Solution is found

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
        solution = self.solve( dict(), 0)
        
        print(solution)
        if( not self.check_solution(solution) ):
            return False

        return solution
