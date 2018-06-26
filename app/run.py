from flask import Flask, render_template
import controllers
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

# config.from_object('config')

client = MongoClient('localhost', 27017)
@app.route('/get_game', methods=['GET'])
def show_game():
	return controllers.get_game()

@app.route('/add_move/<subgame>/<cell>/<symbol>', methods=['POST'])
def add_move(subgame, cell, symbol):
	controllers.add_move_board(subgame, cell, symbol)
	return "Adding stuff to board"

@app.route('/solve', methods=['GET'])
def board_status():
	return str(controllers.solve_single_board())

# @app.route('/frontend', methods=['GET'])
# def solve():
# 	return render_template('ui.html')
app.run(host='0.0.0.0', port=8080, debug=True)
