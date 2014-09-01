# Tic Tac Toe + AI

import random

def drawBoard(board):
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')

def inputPlayerLetter():
	letter  = ''
	while not (letter == 'X' or letter == 'O'):
		letter = raw_input('Do you want to be X or O? ').upper()


