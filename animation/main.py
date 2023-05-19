from animation import Animation
from best_first_search import Best_First_Search, Variants
from Graph import CustomGraph
if __name__ == "__main__":
    # this graph is just for tesing
    customGraph = {"A": [["B", 2], ["C", 3], 9],  # h(n) to G ,h(n) to F
                   "B": [["A", 2], ["C", 4], ["D", 5], 15],
                   "C": [["A", 3], ["B", 4], ["D", 3], ["F", 6], 13],
                   "D": [["B", 5], ["C", 3], ["E", 2], 6],
                   "E": [["G", 5], ["F", 3], ["D", 2], 4],
                   "F": [["C", 6], ["E", 3], 6],
                   "G": [["E", 5], 0]
                   }
    algo = Best_First_Search(
        "A", ["F"], problem=CustomGraph(customGraph), algorithm=Variants.A_star)
    animate = Animation(algorithm=algo)
    animate.animation_pop_up()
