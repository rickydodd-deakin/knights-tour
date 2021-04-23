'''
    * Warnsdorff's Rule implementation to solve A Knight's Tour problem.
    * Initial state: knight occupies, and has only come in contact, with one tile (the starting tile).
    * Goal state: all tiles have been occupied once and only once.
    * Contributed to by: Patrick Wright
'''
from Shared_Core import *
import matplotlib.pyplot as plt
#from collections import Counter


#empty path
path = []

def Warnsdorff_Implementation(count, position, limit, board_size):
    nextMove = position
    move_list = 0
    critical_point = []
    #set path of starting position to value 'Yes'
    G.nodes[position]['path'] = "yes"
    #append starting position to the final path list
    path.append(position)
    #loop until journey is complete
    while(count < limit-1):
        attempts = 0
        #create a move list from our current position
        move_list = legal_moves(board_size,nextMove)
        #order the list from least neighbours to most neighbours
        orderedNeighbours_dict = Ordering_Neighbours(move_list)
        orderedNeighbours = list(orderedNeighbours_dict.keys())
        #if no options left call first item in critical path, otherwise continue as normal
        if(len(orderedNeighbours) == 0):
            nextMove = no_options_left(attempts, path, orderedNeighbours_values, critical_point)
        else:
            nextMove = orderedNeighbours[0]
        #saving critical points
        if(len(orderedNeighbours) > 1):
            temp_store = 0
            temp_store = save_critical_point(orderedNeighbours_dict)
            if(temp_store != 0):
                critical_point.append(temp_store)
        #traverse list to find square with least neighbours, that has not already been visited
        for p in orderedNeighbours:       
            #if the square has not been visited, set it to be the next move
            if (G.nodes[p]['path'] == "no"):
                nextMove = p
                #move knight to new position and mark it as visited
                G.nodes[nextMove]['path'] = "yes"
                path.append(nextMove)
                #increase counter
                count += 1
                break
    print('final path is ', path)

#this function takes a list of moves from any given position, and returns a ordered list of how many neighbours each move has
def Ordering_Neighbours(move_list):
    d = {}
    sorted_d = {}
    #for every move in the move list
    for m in move_list:
        if(G.nodes[m]['path'] == "no"):
            #set counter to 0
            count = 0
            #get neighbours for current move
            neighbours = [n for n in G.neighbors(m)]
            #count neighbours
            for c in neighbours:
                #problem with path equalling no.
                if(G.nodes[c]['path'] == "no"):    
                    count += 1
            #append to dictionary
            d[m] = count
    #sorting dictionary based on amount of neighbours
    sorted_keys = sorted(d, key=d.get)
    for w in sorted_keys:
        sorted_d[w] = d[w]
    #convert dictionary key's to a list
    #orderedNeighbours = list(sorted_d.keys())
    #return the list
    return sorted_d


def no_options_left(attempts, path, orderedNeighbours_values, critical_point): 
    nextMove = 0
    #if there are no available options left
    if(orderedNeighbours_values == attempts):
        #for potentially the entire path
        for r in path:
            #if the last index in path
            if(path[len(path)-1] != critical_point[attempts]):
                    G.nodes[path.pop()]['path'] = "no"
            else: 
                nextMove = critical_point[attempts]
                critical_point[attempts] = null
                attempts += 1
                break
    return nextMove

def save_critical_point(orderedNeighbours_dict):
        new_restore_point = 0
        #take the dict, separate keys and values for comparison
        orderedNeighbours_keys = list(orderedNeighbours_dict.keys())
        orderedNeighbours_values = list(orderedNeighbours_dict.values())
        #if theres another move with equal num of neighbours, store it as a critical point, break after first value added
        for i in orderedNeighbours_values:
            counter = 0
            if(orderedNeighbours_values[counter] == orderedNeighbours_values[counter+1]):
                new_restore_point = orderedNeighbours_keys[counter+1]
                break
        return new_restore_point
        
