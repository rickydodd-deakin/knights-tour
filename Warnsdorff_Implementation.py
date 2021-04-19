'''
    * Warnsdorff's Rule implementation to solve A Knight's Tour problem.
    * Initial state: knight occupies, and has only come in contact, with one tile (the starting tile).
    * Goal state: all tiles have been occupied once and only once.
    * Contributed to by: Patrick Wright
'''
from Shared_Core import *
import matplotlib.pyplot as plt

#empty path
path = []

def Warnsdorff_Implementation(count, position, limit, board_size):
    #set path of starting position to value 'Yes'
    G.nodes[position]['path'] = "yes"
    #append starting position to the final list
    path.append(position)
    #print('the current path is', path)
    #create move list for starting position
    move_list = legal_moves(board_size, position)
    #loop until journey is complete
    for i in range(limit-1):
        #print('move_list now includes', move_list)
        #initially set minimum to first element in possibility list
        minimum = move_list[0]
        #traverse list to see if there is a minimum smaller than current minimum
        for p in move_list:       
            #if length of p is less or equal to length of minimum, update minimum to equal p
            if (len(p) <= len(minimum) and G.nodes[p]['path'] == "no"):
                minimum = p
                #print('minimum is now set to', minimum)     
        #move knight to new position and mark it as visited
        move_list = legal_moves(board_size, minimum)
        G.nodes[minimum]['path'] = "yes"
        path.append(minimum)
        #increase counter
        count += 1
    print('final path is ', path)


