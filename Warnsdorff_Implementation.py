'''
    * Warnsdorff's Rule implementation to solve A Knight's Tour problem.
    * Initial state: knight occupies, and has only come in contact, with one tile (the starting tile).
    * Goal state: all tiles have been occupied once and only once.
    * Contributed to by: Patrick Wright
'''
#change starting cell to 1
chess_board = [[1,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0]]

def print_board():
    for i in range(8):
        for j in range(8):
            print(chess_board[i][j], end=" ")
        print("\n")


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
            #print(x+possible_x[i], y+possible_y[i])
    
    return possibilities

def solve():
    #start counter from second position
    counter = 2
    x = 0
    y = 0
    #in a 8x8 loop 63 times (we already have position 1)
    for i in range(63):
        #start from 0,0
        pos = get_possibilities(x, y)
        #initially set minimum to first element in possibility list
        minimum = pos[0]
        #traverse list to see if there is a minimum smaller than current minimum
        for p in pos:
            if len(get_possibilities(p[0], p[1])) <= len(get_possibilities(minimum[0], minimum[1])):
                minimum = p
        #move knight to new position
        x = minimum[0]
        y = minimum[1]
        chess_board[x][y] = counter
        counter += 1

solve()
print_board()