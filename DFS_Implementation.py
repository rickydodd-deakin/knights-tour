'''
    * Depth-first search implementation to solve A Knight's Tour problem.
    * Initial state: knight occupies, and has only come in contact, with one tile (the starting tile).
    * Goal state: all tiles have been occupied once and only once.
    * Contributed to by: Ricky Dodd (220010849)
'''
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
path = [] # list and, when the goal state is achieved, it will contain the successful path

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

'''
    perform_tour(n, u, limit) take the arguments n, u, and limit, such that n is 0, u is the tuple (row,column)
    corresponding to a knight game piece, and limit is the total number of tiles of the board.
    Returns a boolean value of True when the goal state is achieved.
'''
def perform_tour(n, u, limit):
    # attribute names are used to differentiate between what's currently *considered* (tension of considered)
    # part of the correct path and what hasn't been searched (or been deemed not the correct vertex if variable i
    # has stepped over it).
    G.nodes[u]['path'] = "yes"
    path.append(u)

    if n < limit:
        connected_list = [item for item in G.neighbors(u)]
        i = 0
        goal_state = False
        while i < len(connected_list) and not goal_state:
            if G.nodes[connected_list[i]]['path'] == "no": # neighbor list
                goal_state = perform_tour(n+1, connected_list[i], limit)
            i = i + 1 # move along the neighbor list
        if not goal_state: # not the goal state, traceback.
            G.nodes[path.pop()]['path'] = "no"
    else:
        goal_state = True
    return goal_state
