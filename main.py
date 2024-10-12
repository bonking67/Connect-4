# There are two players, who play on alternating turns
# Each player must select a column to put their piece in
# Win conditions:
  # 1. The board gets filled up and no one wins (a draw/tie)
  # 2. One of the two players connects 4 dots in a row horizontally, vertically, or diagonally and wins the game.

# 1. Make the board (6 rows x 7 columns)
"""
items = [[1, 2, 3],
         [4, 5, 6]]

print(items[0])

first_row = items[0]
print(first_row)

print(first_row[2])
print(items[0][2])

print(items[1][1])
"""

EMPTY_PIECE = '.'

board = [[EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
         [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
         [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
         [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
         [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE],
         [EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE, EMPTY_PIECE]]

# 2. Create function print_board to nicely print out the current state of the board as a string
"""
0 0 0
0 0 0
0 0 0
"""
def print_board():
    print("\n")
    for y in range(6):
        Row = ""
        for x in range(7):
            Row += str(board[y][x]) + " "
        print(Row)
    print("\n")
    
print_board()

# 3. Define the player tokens
player_1 = input("Player 1: Please enter your player token. ")
while True:
    player_2 = input("Player 2: Please enter your player token. ")
    if player_1 == player_2:
        print("You cannot choose the same token as player 1. Please try again.")
        print("________________________________________________________________")
    else:
        break


# 4. Define a variable called turn that we can use to keep track of which player's turn it is
turn = 1

# 5. Write a function that uses the turn number and returns which player should go
def player_turn():
    if turn % 2 == 1:
        return player_1
    else:
        return player_2

# 8. Write a function called drop_piece() that places the token into the eventual correct location based on the column chosen
def drop_piece(column):
    column = column - 1
    # Loop through the rows of board by index
    for row in range(len(board)):
        # Only place the piece down if a certain condition is true
        if check_placement(row, column) == False:
            print("That is not a valid placement.")
            break
        row = row*-1-1
        if board[row][column] == EMPTY_PIECE:
            board[row][column] = player_turn()
            break
            
# 9. Write a function check_placement() that given a row and a column
# returns True or False based on whether it is a valid placement (not out of bounds)
def check_placement(row, column):
    if column>7 or column<0:
        return False
    elif row>6 or row<0:
        return False
    else:
        return True

# 10. is_board_filled() 
# return False if there is still empty space on the board or True if there is not
def is_board_filled():  
    for x in range(6):
        for y in range(7):
            current_square = board[x][y]
            if current_square == EMPTY_PIECE:
                return False
    return True


# 11. is_horizontal_win()
# Takes one parameter, a player's token and return True if the player wins by matching 4 of their own tokens in a horizontal row
# otherwise, return False

# Usage:
# is_horizontal_win(1)  # Checks if player 1 has 4 in a row horizontally
# is_horizontal_win(2)  # Checks if player 2 has 4 in a row horizontally
def is_horizontal_win(player):
    # Try just a single row to start.
    # How to check if we have 2 of the same symbol in a row?
    # row = [1,2,0,2,2,2,2]
    y=0
    x=0
    while y <= 5:
        row = board[y]
        while x <= 3:
            if row[x] == player and row[x+1] == player and row[x+2] == player and row[x+3] == player: 
                return True
            else:
                x += 1
        x = 0
        y += 1
    return False

def is_vertical_win(player):
    y=0
    x=0
    while y <= 2:
        while x <= 6:
            if board[y][x] == player and board[y+1][x] == player and board[y+2][x] == player and board[y+3][x] == player:
                return True
            else: 
                x += 1
        y += 1    
        x = 0
    return False

# 0,0 1,1 2,2 3,3
# 0,1 1,2 2,3 3,4
# 0,2,1,3 1,4 1,5

# 1,0 2,1 3,2 4,3
# 2,0 3,1 4,2 5,3

def is_diagonal_win_topleft(player):
    y=0
    x=0
    while y <= 2:
        while x <= 3:
            if board[y][x] == player and board[y+1][x+1] == player and board[y+2][x+2] == player and board[y+3][x+3] == player:
                return True
            else:
                x += 1
        x = 0
        y += 1
    return False

def is_diagonal_win_topright(player):
    y=0
    x=0
    while y >= -3:
        while x <= 4:
            if board[y-1][x] == player and board[y-2][x+1] == player and board[y-3][x+2] == player and board[y-4][x+3] == player:
                return True
            else:
                x += 1
        x = 0
        y -= 1
    return False
        
def player_has_won():
    # if is_horizontal_win(player_turn()) or is_vertical_win(player_turn()) or is_diagonal_win_topleft(player_turn()) or is_diagonal_win_topright(player_turn()):
    #     return True
    # return False

    if is_horizontal_win(player_turn()):
        print("Player {} won horizontally, the game is over!". format(player_turn()))
        return True

    if is_vertical_win(player_turn()):
        print("Player {} won vertically, the game is over!". format(player_turn()))
        return True

    if is_diagonal_win_topleft(player_turn()):
        print("Player {} won diagonally, the game is over!". format(player_turn()))
        return True

    if is_diagonal_win_topright(player_turn()):
        print("Player {} won diagonally, the game is over!". format(player_turn()))
        return True

    return False
  


# 6. Set up a while loop with the condition while True to represent all repeating turns
while True:
    # 7. For each turn, prompt the player to enter the column they wish to place their piece in, and store it in a variable called column
    column = int(input("\nPlayer {} turn \n Where do you want to put your token? Column: ".format(player_turn())))
    drop_piece(column)    
    print_board()
    
    if player_has_won():
        break

    turn += 1
    if is_board_filled() == True:
        print("The board is filled, the game is over!")
        break
        




"""
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
"""