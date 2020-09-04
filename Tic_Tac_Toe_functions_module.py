import itertools
import time
from colorama import Fore, Back, Style, init


init()

def win(current_game, player):

	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False

	# Horizontal
	for row in current_game:
		if all_same(row):
			print(f"Congratulations! {player} is the winner horizontally (-)!")
			return True

	# Diagonal
	diags = []
	for col, row in enumerate(reversed(range(len(current_game)))):
		diags.append(current_game[row][col])
	if all_same(diags):
		print(f"Congratulations! {player} is the winner diagonally (/)!")
		return True

	diags = []
	for ix in range(len(current_game)):
		diags.append(current_game[ix][ix])
	if all_same(diags):
		print(f"Congratulations! {player} is the winner diagonally (\\)!")
		return True

	# Vertical
	for col in range(len(current_game)):
		check = []
		for row in current_game:
			check.append(row[col])
		
		if all_same(check):
			print(f"Congratulations! {player} is the winner vertically (|)!")
			return True

	return False


def full(c_game):

	l = []
	for row in c_game:
		if row.count(0) == 0:
			l.append("t")
	if l.count("t") == 3:
		print("DRAW!")
		return True


def game_board(game_map, player=0, row=0, column=0, just_display=False):
	try:
		if game_map[row][column] != 0:
			print("This position is occupado! Choose another!")
			return game_map, False

		print("   "+"  ".join([str(i+1) for i in range(len(game_map))]))

		if not just_display:
			game_map[row][column] = player

		for count, row in enumerate(game_map):
			colored_row = ""
			for item in row:
				if item == 0:
					colored_row += "   "
				elif item == 1:
					colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
				elif item == 2:
					colored_row += Fore.MAGENTA + ' Y ' + Style.RESET_ALL

			print(count+1, colored_row)



		return game_map, True

	except IndexError as e:
		print("Error: make sure you input row/column correct: \n", e)

	except Exception as e:
		print("Something went wrong. solve the problem and retry: \n", e)
		return game_map, False