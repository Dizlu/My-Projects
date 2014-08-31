from random import randint

board = []

for x in range(0, 10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def creating_fleet(board):
    ships = {'four': {}, 'three': {} , 'two': {} , 'one': {}}
    print "Tutaj widzimy wylosowane stateczki"
    board_ships = print_board(board)
    while len(ships['four']) < 1:
        ships ['four'][randint(1, len(board))] = randint(1, len(board[0]))
        a = int(ships['four'].keys()[0])
        b = int(ships['four'].values()[0])
        print a , b
        
    return ships, board_ships


fleet = creating_fleet(board)
print fleet

for turn in range(6):
    print "Turn", turn +  1
    print "Choose from 1- 10."
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    guess_row1 = guess_row - 1
    guess_col1 = guess_col - 1

    left_ones = len(fleet) - 1 
    if guess_row in fleet and guess_col in fleet.values():                    
        print "Congratulations! You sank my battleship!"
        board[guess_row1][guess_col1] = "X"
        fleet.pop(guess_row, None)
        print print_board(board)
        if left_ones == 0:
            print "Nice win, sailor!"
            print "You sank my whole fleet!"
            break
    else:
        if guess_row not in range(10) or \
        guess_col not in range(10):
            print "Oops, that's not even in the ocean."
        elif board[guess_row1][guess_col1] == "X":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row1][guess_col1] = "X"
            print print_board(board)

if turn == 5:
    print "Game Over"
    print "The rest of my fleet was at:", fleet, "."