import itertools
from time import sleep
from colorama import Fore, Back, Style, init
import random
import subprocess as sp

init()

from Tic_Tac_Toe_functions_module import win, full, game_board

game_mode = int(input("Choose the game mode: \n(Play with computer: 1) \n(Play multiplayer: 2) \n"))

if game_mode == 1:
    play = True
    name_input = False
    player1_wins = 0
    player2_wins = 0
    try:
        while not name_input:
            player = input("\nEnter username: ")
            if player != "PC":
                name_input = True
            else:
                print("Make sure you didn't put \"PC\" and put it again.")
        first_one = int(input("who goes first? (You: 1, PC: 2) "))
        players = [player, "PC"]
        if first_one == 2:
            players = list(reversed(players))

        while play:
            sleep(0.4)
            game_size = int(input("\nWhat size of Tic Tac Toe? "))
            print()
            game = [[0 for i in range(game_size)] for i in range(game_size)]
            game_won = False
            game, _ = game_board(game, just_display=True)
            player_choice = itertools.cycle(players)

            while not game_won:
                current_player = next(player_choice)
                print(f"Current player: {current_player}")
                print()
                played = False

                while not played:
                    if current_player == "PC":
                        possible_rows_list = []
                        possible_columns_list = []
                        counter = 0

                        while counter <= 9:
                            for row in range(len(game)):
                                for col in range(len(game)):
                                    counter += 1
                                    if game[row][col] == 0:
                                        possible_rows_list.append(row)
                                        possible_columns_list.append(col)

                        played = True

                        possible_choices = [(row, column) for row, column in zip(possible_rows_list, possible_columns_list)]
                        rand_ix_choice = random.choice(range(len(possible_choices)))
                        PC_column_choice = possible_choices[rand_ix_choice][1]
                        PC_row_choice = possible_choices[rand_ix_choice][0]
                        game, played = game_board(game, players.index(current_player)+1, PC_row_choice, PC_column_choice)
                        print()

                        played = True
                    elif current_player == player:
                        sleep(0.4)
                        player_column_choice = int(input("What column do you want to play? "))
                        player_row_choice = int(input("What row do you want to play? "))
                        sleep(0.4)
                        tmp = sp.call('cls', shell=True)
                        game, played = game_board(game, players.index(current_player)+1, player_row_choice-1, player_column_choice-1)
                        print()

                if win(game, current_player):
                    if current_player == player: player1_wins += 1
                    if current_player == "PC": player2_wins += 1
                    print(f"\n{player} {player1_wins} - {player2_wins} PC\n")
                    game_won = True
                    sleep(0.4)
                    again = input("The game is over...\nContinue this game: c\nRestart: r\nQuit: q\n")
                    if again.lower() == 'c':
                        print("\nStaring the next round...")
                    elif again.lower() == 'r':
                        player1_wins, player2_wins = 0, 0
                        print("\nRestarting...")
                    elif again.lower() == 'q':
                        print("\nByeeeeee")
                        play = False
                    else:
                        print("Not a valid answer, so... see you later :)")
                        play = False
                elif full(game):
                    print(f"\n{player} {player1_wins} - {player2_wins} PC\n")
                    game_won = True
                    sleep(0.4)
                    again = input("The game is over, would you like to play again? (y/n) ")
                    if again.lower() == 'y':
                        print("\nRestarting...")
                    elif again.lower() == 'n':
                        print("\nByeeeeee")
                        play = False
                    else:
                        print("Not a valid answer, so... see you later :)")
                        play = False
    except Exception as e:
        print("Something went wrong. solve the problem and retry: \n", e)


elif game_mode == 2:
    play = True
    names_input = False
    player1_wins = 0
    player2_wins = 0
    try:
        while not names_input:
            sleep(0.4)
            player1 = input("\nPlayer one name: ")
            player2 = input("Player two name: ")
            if player1 != player2:
                names_input = True
            else:
                print("Make sure you used different names and put them again.")
        first_one = int(input("Who goes first? (player 1: 1, player 2: 2) "))
        players = [player1, player2]
        if first_one == 2:
            players = list(reversed(players))

        while play:
            sleep(0.4)
            game_size = int(input("\nWhat size of Tic Tac Toe? "))
            print()
            game = [[0 for i in range(game_size)] for i in range(game_size)]
            playing = True
            game, _ = game_board(game, just_display=True)
            player_choice = itertools.cycle(players)

            while playing:
                current_player = next(player_choice)
                print(f"Current player: {current_player}")
                print()
                played = False

                while not played:
                    sleep(0.4)
                    column_choice = int(input("What column do you want to play? "))
                    row_choice = int(input("What row do you want to play? "))
                    sleep(0.4)
                    game, played = game_board(game, players.index(current_player)+1, row_choice-1, column_choice-1)
                    print()

                if win(game, current_player) or full(game):
                    if current_player == player1: player1_wins += 1
                    if current_player == player2: player2_wins += 1
                    print(f"\n{player1} {player1_wins} - {player2_wins} {player2}\n")
                    playing = False
                    sleep(0.4)
                    again = input("The game is over, would you like to play again? (y/n) ")
                    if again.lower() == 'y':
                        print("\nRestarting...")
                    elif again.lower() == 'n':
                        print("\nByeeeeee")
                        play = False
                    else:
                        print("Not a valid answer, so... see you later :)")
                        play = False

    except Exception as e:
        print("Something went wrong. solve the problem and retry: \n", e)

