import itertools

# Checking that items in defined position is the same or not

def all_same(l):
        if (l.count(l[0]) == len(l)) and (l[0] != 0):
            print(f"Player {l[0]} is the winner!")
            return True
        else:
            return False
# Checking that there is winner or not
def win(current_game):
    
    # Horizontal position

    for row in current_game:
        return_value = all_same(row)
        if return_value:
            return True


    # Vertical position

    trans_game = list(zip(*current_game))
    for t_row in trans_game:
        return_value = all_same(t_row)
        if return_value:
            return True

    # Diagnol position

    diag = []
    for col, row in enumerate(reversed(range(len(current_game)))):
        diag.append(current_game[row][col])
    return_value = all_same(diag)
    if return_value:
            return True

    diag = []
    for ix in range(len(current_game)):
        diag.append(current_game[ix][ix])
    return_value = all_same(diag)
    if return_value:
            return True

    
    return return_value

# Draw board of game

def game_board(game_map, player=0, row=0, column=0):
    try:
        if game_map[row][column] != 0:
            print("This position is occupado! Choose another position...")
            return game_map, False

        print("   0  1  2")
        game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as e:
        print("'Make sure input row/column as 0 or 1 or 2'", e)
        return game_map, False
    except Exception as e:
        print("Somethings went wrong!!", e)
        return game_map, False
    '''else:
        print("Somethings went wrong!!")
    finally:
        print("Somethings went wrong!!")'''

play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    game_won = False
    finish_game = False
    game, _ = game_board(game)
    player_choice = itertools.cycle([1,2])

    while (not game_won) and (not finish_game):
        current_player = next(player_choice)
        print(f"current_player: {current_player}")
        played = False

        while not played:
            
            col_choice = int(input("What column do you want to choose? (0, 1, 2): "))
            row_choice = int(input("What row do you want to choose? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, col_choice)
            

            # Checking that there is winner or not

            if win(game):
                game_won = True
                again = input("game's over, do you like play again? (y/n) ")
                if again.lower() == 'y':
                    print("Restarting...")
                elif again.lower() == 'n':
                    print("Enjoy your Moments, Bye...")
                    play = False
                else:
                    print("Not a valid answer...")
                    play = False
                
            # Checking that there is no options to choose for finishing game without winner

            N=0
            for item in game:
               if 0 not in item:
                   N+=1
            if N == len(game):

                played = True
                finish_game = True
                again = input("Game is over, without any winner..., do you like play again? (y/n) ")
                if again.lower() == 'y':
                    print("Restarting...")
               
                elif again.lower() == 'n':
                    print("Enjoy your Moments, Bye Bye...")
                    play = False
                    
                else:
                    print("Not a valid answer...")
                    play = False