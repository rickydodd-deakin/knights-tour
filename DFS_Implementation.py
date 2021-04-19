'''
    * Depth-first search implementation to solve A Knight's Tour problem.
    * Initial state: knight occupies, and has only come in contact, with one tile (the starting tile).
    * Goal state: all tiles have been occupied once and only once.
    * Contributed to by: Ricky Dodd (220010849)
'''
import matplotlib.pyplot as plt
import networkx as nx
from Shared_Core import *

path = [] # list and, when the goal state is achieved, it will contain the successful path

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
