'''
    * A shared core for both implementations. Both leverage these functions.
    * Contributed to by: Ricky Dodd (220010849)
'''

import networkx as nx
G = nx.Graph()

'''
    generate_graph(board_size) takes an argument board_size, such that it is an integer n where n^2 gives the
    total board tiles.
    Results in G containing a complete graph of the board from the perspective of a knight piece.
'''
def generate_graph(board_size):
    for r in range(board_size):
        for c in range(board_size):
            G.add_node((r,c), path='no')
            for move in legal_moves(board_size, (r,c)):
                G.add_node(move, path='no')
                G.add_edge((r,c), move)

    return

'''
    legal_moves(board_size, knight_pos) take arguments board_size and knight_pos, corresponding to an integer n
    such that n^2 gives the total board tiles and knight_pos is a tuple of (row,column).
    Returns an array of legal moves (not outside the game-space) from that particular position.
'''
def legal_moves(board_size, knight_pos):
    l_m = [] # list of legal moves

    # all moves, legal or not
    moves = [(knight_pos[0]-2, knight_pos[1]-1), (knight_pos[0]-2, knight_pos[1]+1),
        (knight_pos[0]+2, knight_pos[1]-1), (knight_pos[0]+2, knight_pos[1]+1),
        (knight_pos[0]-1, knight_pos[1]-2), (knight_pos[0]-1, knight_pos[1]+2),
        (knight_pos[0]+1, knight_pos[1]-2), (knight_pos[0]+1, knight_pos[1]+2)]
    
    # checking they abide to the confines of the game board, appending to list l_m if they do
    for element in moves:
        if (element[0] >= 0 and element[0] < board_size):
            if (element[1] >= 0 and element[1] < board_size):
                l_m.append(element)

    return l_m