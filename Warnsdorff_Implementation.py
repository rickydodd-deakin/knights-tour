'''
    * Warnsdorff's Rule implementation to solve A Knight's Tour problem.
    * Initial state: knight occupies, and has only come in contact, with one tile (the starting tile).
    * Goal state: all tiles have been occupied once and only once.
    * Contributed to by: Patrick Wright
'''
from Shared_Core import *
import matplotlib.pyplot as plt
from collections import Counter


#empty path
path = []
'''
def Warnsdorff_Implementation(count, position, limit, board_size):
    nextMove = position
    #set path of starting position to value 'Yes'
    G.nodes[position]['path'] = "yes"
    #append starting position to the final list
    path.append(position)
    #get first move_list based on starting position
    move_list = legal_moves(board_size, position)
    #loop until journey is complete
    if count < limit:
        #create a move list from our current position
        move_list = legal_moves(board_size,nextMove)
        print('move list is', move_list)
        #order the list from least neighbours to most neighbours
        orderedNeighbours = Ordering_Neighbours(move_list)
        print('ordered neighbours is',orderedNeighbours)
        #initially set the next move to be the first square in the ordered neighbours list
        nextMove = orderedNeighbours[0]
        #traverse list to find square with least neighbours, that has not already been visited
        for p in orderedNeighbours:       
            #if the square has not been visited, set it to be the next move
            if (G.nodes[p]['path'] == "no"):
                nextMove = p
                print('next move is', nextMove)
                #move knight to new position and mark it as visited
                G.nodes[nextMove]['path'] = "yes"
                print('adding next move to path of: ', nextMove)
                path.append(nextMove)
                #increase counter
                count += 1
                break
        
    print('final path is ', path)
'''
#this function takes a list of moves from any given position, and returns a ordered list of how many neighbours each move has
def Ordering_Neighbours(move_list):
    d = {}
    sorted_d = {}
    #for every move in the move list
    for m in move_list:
        #set counter to 0
        count = 0
        #get neighbours for current move
        neighbours = [n for n in G.neighbors(m)]
        #count neighbours
        for c in neighbours:
            count += 1
        #append to dictionary
        d[m] = count
    #sorting dictionary based on amount of neighbours
    sorted_keys = sorted(d, key=d.get)
    for w in sorted_keys:
        sorted_d[w] = d[w]
    #convert dictionary key's to a list
    orderedNeighbours = list(sorted_d.keys())
    #return the list
    return orderedNeighbours


def Warnsdorff_Implementation(n, u, limit, board_size):
    # attribute names are used to differentiate between what's currently *considered* (tension of considered)
    # part of the correct path and what hasn't been searched (or been deemed not the correct vertex if variable i
    # has stepped over it).
    G.nodes[u]['path'] = "yes"
    path.append(u)

    if n < limit:
        ordered_list = Ordering_Neighbours(legal_moves(board_size,u))
        print('ordered list is: ', ordered_list,'at move number', n)
        i = 0
        goal_state = False
        while i < len(ordered_list) and not goal_state:
            if G.nodes[ordered_list[i]]['path'] == "no": # neighbor list
                goal_state = Warnsdorff_Implementation(n+1, ordered_list[i], limit, board_size)
            i = i + 1 # move along the neighbor list
        if not goal_state: # not the goal state, traceback.
            G.nodes[path.pop()]['path'] = "no"
    else:
        goal_state = True
    return goal_state
