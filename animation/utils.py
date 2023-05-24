from enum import Enum


# we can add more similar algorithms
# this is an Enum for the variannts of the best first search techniques
class Variants(Enum):
    UCS = 1
    A_star = 2
    GREEDY = 3
    BFS = 4
    DFS = 5
    DPL = 6
    IDS = 7
    BEAM = 8
    HILL = 9

