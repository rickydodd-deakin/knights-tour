'''
    * Warnsdorff's Rule implementation to solve A Knight's Tour problem.
    * Initial state: knight occupies, and has only come in contact, with one tile (the starting tile).
    * Goal state: all tiles have been occupied once and only once.
    * Contributed to by: Patrick Wright
'''
from Shared_Core import *
import matplotlib.pyplot as plt
#change starting cell to 1
'''
#this is the hardcoded 8x8 board i started with
#the starting cell for the knight is set to 1
#to be updated with Ricky's utility method
chess_board = [[1,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0]]

#define boardsize here
#board_size = 8


#this method prints the current state of the board
def print_board():
    for i in range(8):
        for j in range(8):
            print(chess_board[i][j], end=" ")
        print("\n")


#this method gets the current possibilities - update with Ricky's method

def get_possibilities(x, y):
    #possible moves
    possible_x = (2, 1, 2, 1, -2, -1, -2, -1)
    possible_y = (1, 2, -1, -2, 1, 2, -1, -2)
    #empty list to store possibilities
    possibilities = []
    #if at positions listed as x & y, print possible cells to move to
    for i in range(8):
        #check to ensure cell is inside the board and not already used
        if x+possible_x[i] >= 0 and x+possible_x[i] <= 7 and y+possible_y[i] >= 0 and y+possible_y[i] <= 7 and chess_board[x+possible_x[i]][y+possible_y[i]] == 0:
            possibilities.append([x+possible_x[i], y+possible_y[i]])   
    return possibilities
'''
#empty path
path = []

def Warnsdorff_Implementation(count, position, limit, board_size):
    #set path of starting position to value 'Yes'
    G.nodes[position]['path'] = "yes"
    #append starting position to the final list
    path.append(position)
    print('the current path is', path)
    #create move list for starting position
    move_list = legal_moves(board_size, position)
    #loop until journey is complete
    for i in range(limit):
        print('move_list now includes', move_list)
        #initially set minimum to first element in possibility list
        minimum = move_list[0]
        print('minimum is now set to', minimum)
        #traverse list to see if there is a minimum smaller than current minimum
        for p in move_list:       
            #if length of p is less or equal to length of minimum, update minimum to equal p
            if (len(p) <= len(minimum)):
                minimum = p
        #move knight to new position and mark it as visited
        move_list = legal_moves(board_size, minimum)
        G.nodes[minimum]['path'] = "yes"
        path.append(minimum)
        #increase counter
        count += 1
    print('final path is ', path)

'''
def solve():
    counter = 2
    x = 0
    y = 0
    for i in range(63):
        pos = get_possibilities(x, y)
        minimum = pos[0]
        for p in pos:
            if len(get_possibilities(p[0], p[1])) <= len(get_possibilities(minimum[0], minimum[1])):
                minimum = p
        x = minimum[0]
        y = minimum[1]
        chess_board[x][y] = counter
        counter += 1

solve()
print_board()
'''