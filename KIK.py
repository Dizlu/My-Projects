print "Pre- alpha version for a couple of fully reasonable beings"

from random import randint

board = [[1,2,3], [4,5,6], [7,8,9]]

def print_game(board):
	for element in board:
		print ""
		for skurwysyn in element:
			print skurwysyn,
	print ""

def choosing():
	choose = int(raw_input("Select your oponent: HUMAN or COMPUTER "))
	choose = choose.upper()
	if choose == "HUMAN":
		print "Take your friend, come and play!"
		return True
	elif choose == "COMPUTER":
		print "Come at me bro!"
		return False
	else:
		print "Hey, that's not a valid opponent."

def who_goes_first():
	if random.randint(0, 1) == 0:
		return "COMPUTER"
	else:
		return "HUMAN"

def computer_thinking():
	return "lol"

def trying_out(digit):
	try:
		int(digit)
		return True
	except ValueError:
		return False

def rotation_X(board):
	check(board, X)
	if check(board, X) == True:
		print_game(board)
		move = int(raw_input("Shot! [Player 1]: "))
		one = (move - 1) / 3
		two = (move - 1) % 3
		if trying_out(board[one][two]) == True:
			board[one][two] = "X"
		else:
			print "Choose another one Player 1!"
			move2 = int(raw_input("Take another shot cowboy! [Player 1]: "))
			one2 = (move2 - 1) / 3
			two2 = (move2 - 1) % 3
			if trying_out(board[one2][two2]) == True:
				board[one2][two2] = "X"
			else:
				print "Okay that's enough! You're losing a turn!"

def rotation_O(board):
	check(board, 'O')
	if check(board, 'O') == True:
		print_game(board)
		opponent_move = int(raw_input("Shot! [Player 2]: "))
		one1 = (opponent_move - 1) / 3
		two1 = (opponent_move - 1) % 3
		if trying_out(board[one1][two1]) == True:
			board[one1][two1] = "O"
		else:
			print "Choose another one Player 2!"
			move3 = int(raw_input("Take another shot cowboyaa second one! [Player 2]: "))
			one3 = (move3 - 1) / 3
			two3 = (move3 - 1) % 3
			if trying_out(board[one3][two3]) == True:
				board[one3][two3] = "O"
			else:
				print "Okay that's enough! You're losing a turn!"

def check(board, "X"):
	if board[0] == ["X", "X", "X"] or board[1] == ["X", "X", "X"] or board[2] == ["X", "X", "X"]:
		print "You've won Player 1!"
		return False
	elif (board[0][0] == "X" and board[1][0] == "X" and board[2][0]) == "X":
		print "You've won Player 1!"
		return False
	elif (board[0][1] == "X" and board[1][1] == "X" and board[2][1]) == "X":
		print "You've won Player 1!"
		return False
	elif (board[0][2] == "X" and board[1][2] == "X" and board[2][2]) == "X":
		print "You've won Player 1!"
		return False
	elif (board[0][0] == "X" and board[1][1] == "X" and board[2][2]) == "X":
		print "You've won Player 1!"
		return False
	elif (board[2][0] == "X" and board[1][1] == "X" and board[0][2]) == "X":
		print "You've won Player 1!"
		return False
	else:
		return True

def main():
	check_X(board, "X")
	check_X(board, "O")
	turn = 0
	while check(board, "X") == True and check(board, "O") == True:
		turn += 1
		print ""
		if turn % 2 != 0:
			print "Turn ", turn
			rotation(board, "X")
		elif turn % 2 == 0:
			print "Turn ", turn
			rotation(board, "O")
main()
		

