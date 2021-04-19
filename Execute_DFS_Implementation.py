'''
    * Executes depth-first-search on a six-by-six game board.
    * It is *not* recommended this is ran, unlesss you have a lot of time.
    * Contributed to by: Ricky Dodd (220010849)
'''

from DFS_Implementation import *

'''
    perform_dfs() generates a graph for a 6 x 6 board, by calling generate_graph(), and then performs a tour
    on that graph, by calling perform_tour(), and then prints the results upon termination.
'''
def perform_dfs():
    generate_graph(6)
    perform_tour(0, (0,0), len(G))
    print(path)
    return

perform_dfs()