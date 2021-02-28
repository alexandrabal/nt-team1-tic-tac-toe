import logging
from .gameengine import game_start

logger = logging.getLogger(__name__)

"""
The functionality will add support for single game only
Will add support for 2/3 games. The winner will be the one who wins 2 out of maximum 3 games
3/5 The winner will be the one who wins 3 out of maximum 5 games"""

question = "Please enter a Game Mode: - How many rounds do you wish to play -  1, 3 or 5?"

def check_player_choice():
    number_of_games = 0
    valid_number_of_games = False
    while valid_number_of_games == False:
        try:
            number_of_games = int(input(question))
            if number_of_games == 1 or number_of_games == 3 or number_of_games == 5:
                valid_number_of_games == True
                print(number_of_games, "Rounds - Let's go!")
            else:
                print("Oops that's not a valid GAME MODE")
                logger.error("Oops that's not a valid GAME MODE")
                logger.exception(e)
        except ValueError:
            print("Oops that's not a valid GAME MODE")
            logger.error("Oops that's not a valid GAME MODE")
            logger.exception(e)
        return number_of_games

def play_rounds(how_many_rounds):
    for i in range(0,how_many_rounds):
        game_start()