from random import randint

board = []

for x in range(0, 10):
    board.append(["O"] * 10)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

#def testing(a, b):
    #try:
        #board[a + (x in range (-1, 2))][b + (y in range(-1, 2))] == "X"
        #return True
    #except ValueError:
        #return Falsepyt

def creating_ones(board):
    ones = {}
    while len(ones) < 5:
        ones [randint(1, len(board))] = randint(1, len(board[0]))  
    return ones
ship_ones = creating_ones(board)
print ship_ones

def test():
    x = []
    y = []
    for key, value in ship_ones.iteritems():
        x.append(key)
        x.append(key - 1)
        x.append(key - 1)
        x.append(key - 1)
        x.append(key)
        x.append(key)
        x.append(key + 1)
        x.append(key + 1)
        x.append(key + 1)
        y.append(value)
        y.append(value -1)
        y.append(value)
        y.append(value + 1)
        y.append(value - 1)
        y.append(value + 1)
        y.append(value - 1)
        y.append(value)
        y.append(value + 1)
    chosen = {}
    return x, y

for turn in range(6):
    print "Turn", turn +  1
    print "Choose from 1- 10."
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    guess_row1 = guess_row - 1
    guess_col1 = guess_col - 1

    left_ones = len(ship_ones) - 1 
    if guess_row in ship_ones and guess_col in ship_ones.values():                    
        print "Congratulations! You sank my battleship!"
        board[guess_row1][guess_col1] = "X"
        ship_ones.pop(guess_row, None)
        print left_ones
        print print_board(board)
        print ship_ones
        if left_ones == 0:
            print "Nice win, sailor!"
            print "You sank my whole fleet!"
            break
    else:
        if guess_row not in range(10) or \
        guess_col not in range(10):
            print "Oops, that's not even in the ocean."
            print ship_ones
        elif board[guess_row1][guess_col1] == "X":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row1][guess_col1] = "X"
            print print_board(board)
            print ship_ones

if turn == 5:
    print "Game Over"
    print "The rest of my fleet was at:", ship_ones, "."