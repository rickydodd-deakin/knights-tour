'''
    * Executes Warnsdorff's Rule on an eight-by-eight game board.
    * Contributed to by: Patrick Wright
'''
from Warnsdorff_Implementation import *

def perform_warnsdorff():
    board_size = 6

    generate_graph(board_size)
    Warnsdorff_Implementation(0, (0,0), len(G), board_size)
    return

perform_warnsdorff()
