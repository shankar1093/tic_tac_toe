import Solver
from flask import jsonify
import numpy as np

board = [['','',''],['','',''],['','','']]
big_board = [reduce(lambda x,y: x+y, board), reduce(lambda x,y: x+y, board),reduce(lambda x,y: x+y, board),reduce(lambda x,y: x+y, board),reduce(lambda x,y: x+y, board),reduce(lambda x,y: x+y, board),reduce(lambda x,y: x+y, board),reduce(lambda x,y: x+y, board),reduce(lambda x,y: x+y, board)]
s = Solver.Solver(board)
symbol = None
# def solve_board():


def get_game():
	return jsonify(
		board = str(big_board),
		winner = '',
		turn = 'X',
		valid_subgames = "[0,1,2,4]"
		)

def add_move_board(subgame, cell, symbol):
	big_board[int(subgame)][int(cell)]=str(symbol)
	# print big_board

def error_response():
	return jsonify(Error="Invalid id")

def solve_single_board():
	count = 0
	for i in big_board:
		t = np.reshape(i,(3,3)).tolist()
		mat = Solver.Solver(t)
		if mat.has_won("X") == True:
			count+=1
	return count

