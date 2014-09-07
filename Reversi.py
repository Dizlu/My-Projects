# Reversi

import random
import sys

def drawBoard(board):
    HLINE = '  +---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |'

    print('     1   2   3   4   5   6   7   8')
    print(HLINE)

    for y in range(8):
    	print(VLINE)
    	print(y+1, end=' ')
    	for x in range(8):  #zalozenie dla bledu przy None?
    		print('| %s' %(board[x][y]), end=' ')
    	print('|')
    	print(VLINE)
    	print(HLINE)


def resetBoard(board):
	for x in range(8):
		for y in range(8):
			board[x][y] = ' '

	board[3][3] = 'X'
	board[3][4] = 'O'
	board[4][3] = 'O'
	board[4][4] = 'X'


def getNewBoard():
	board = []
	for i in range(8):
		board.append([' '] * 8)

	return board


def isValidMove(board, tile, xstart, ystart):
	if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
		return False

	board[xstart][ystart] = tile

	if tile == 'X':
		otherTile = 'O'
	else:
		otherTile = 'X'

	tilesToFlip = []
	for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
		x += xdirection
		y += ydirection
		if not isOnBoard(x, y):
			continue
		if board[x][y] == tile:
			while True:
				x -= xdirection
				y -= ydirection
				if x == xstart and y == ystart:
					break
				tilesToFlip.append([x][y])

	board[xstart][ystart] = ' '
	if len(tilesToFlip) == 0:
		return False
	return tilesToFlip

def isOnBoard(x, y):
	return x >= 0 and x <= 7 and y >= 0 and y <= 7

def getBoardWithValidMoves(board, tile):
	dupeBoard = getBoardCopy(board)

	for x, y in getValidMoves(dupeBoard, tile):
		dupeBoard[x][y] = ' '
	return dupeBoard

def getValidMoves(board, tile):
	validMoves = []

	for x in range(8):
		for y in range(8):
			if isValidMove(board, tile, x, y) != False:
				validMoves.append([x, y])
	return validMoves

def getScoreofBoard(board):
	xscore = 0
	oscore = 0
	for x in range(8):
		for y in range(8):
			if borad[x][y] == 'X':
				xscore += 1
			if board[x][y] == 'O':
				oscore += 1
	return {'X': xscore, 'O': oscore}

def enterPlayerTile():
	tile = ''
	while not(tile == 'X' or tile == 'O'):
		tile = raw_input('Do you want to be X or O?' ).upper()

	if tile == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def whoGoesFirst():
	if random.randint(0, 1) == 0:
		return 'computer'
	else:
		return 'player'

def playAgain():
	return raw_input('Do you want to play again? (yes or no) ').lower.startswith('y')

def makeMove(board, tile, xstart, ystart):
	tilesToFlip = isValidMove(board, tile, xstart, ystart)

	if tilesToFlip == False:
		return False

	board[xstart][ystart] = tile
	for x, y in tilesToFlip:
		board[x][y] = tile
	return True

def getBoardCopy(board):
	dupeBoard = getNewBoard()

	for x in range(8):
		for y in range(8):
			dupeBoard[x][y] = board[x][y]

	return dupeBoard

def isOnCorner(x, y):
	return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)

def getPlayerMove(board, playerTile):
	DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()

	while True:
		move = raw_input('Enter your move or type quit to end the game, or hints to turn off/ on hints! ').lower()
		if move == 'quit':
			return 'quit'
		if move == 'hints':
			return 'hints'

		if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
			x = int(move[0]) - 1
			y = int(move[1]) - 1
			if isValidMove(board, playerTile, x, y) == False:
				continue
			else:
				break
		else:
			print('That is not a valid move. Type the x digit (1- 8), then the y digit (1-8)')
			print('For example, 81 will be the top- right corner')

	return [x, y]

def getComputerMove(board, computerTile):
	possibleMoves = getValidMoves(board, computerTile)
	random.shuffle(possibleMoves)

	for x, y in possibleMoves:
		if isOnCorner(x, y):
			return [x, y]
		bestScore = -1
		for x, y in possibleMoves:
			dupeBoard = getBoardCopy(board)
			makeMove(dupeBoard, computerTile,x , y)
			score = getSCoreOfBoard(dupeBoard)[computerTile]
			if score > bestScore:
				bestMove = [x, y]
				bestScore = score
		return bestMove