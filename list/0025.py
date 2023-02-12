list_of_games = ['Game One', 'Game Two']
list_of_players = ['Player One', 'Player Two', 'Player Three', 'Player Four']

list_of_game_player_pairs = [[game, player] for game in list_of_games for player in list_of_players]

for game in list_of_games:
    for player in list_of_players:
        print(game + ', ' + player)
    print('------------------------------')

"""
Game One, Player One
Game One, Player Two
Game One, Player Three
Game One, Player Four
------------------------------
Game Two, Player One
Game Two, Player Two
Game Two, Player Three
Game Two, Player Four
------------------------------
"""
