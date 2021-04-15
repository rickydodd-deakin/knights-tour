# Breadth-first search implementation to solve A Knight's Tour problem.
# Initial state: no knight is placed.
# Goal state: all tiles have been occupied once and only once.
# Contributed to by: Ricky Dodd (220010849)

import networkx as nx

# Takes board size n and knight_pos, tuple in the form (row, column) as arguments.
def legal_moves(board, knight_pos):
    l_m = []
    moves = [(knight_pos[0]-2, knight_pos[1]-1), (knight_pos[0]-2, knight_pos[1]+1),
        (knight_pos[0]+2, knight_pos[1]-1), (knight_pos[0]+2, knight_pos[1]+1),
        (knight_pos[0]-1, knight_pos[1]-2), (knight_pos[0]-1, knight_pos[1]+2),
        (knight_pos[0]+1, knight_pos[1]-2), (knight_pos[0]+1, knight_pos[1]+2)]
    
    for element in moves:
        if (element[0] > 0 and element[0] <= board):
            if (element[1] > 0 and element[1] <= board):
                l_m.append(element)
    
    return l_m

print(legal_moves(6, (4,3)))

