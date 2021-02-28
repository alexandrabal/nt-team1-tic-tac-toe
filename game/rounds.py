# Add functionality to allow selecting a game system:
# add support for single game only
# add support for 2/3 (the winner will be the one who wins 2 games out of a maximum of 3)
# add support for 3/5 (the winner will be the one whi wins 3 games out of a maximum of 5)

"""This is an added functionality of the game, has to be applied on the engine
The functionality will add support for single game only
Will add support for 2/3 games. The winner will be the one who wins 2 out of maximum 3 games
3/5 The winner will be the one who wins 3 out of maximum 5 games"""
from .__init__ import start

#gamemode = (input("Hello, what's your name?"))

question = ("Please enter a GAME MODE: - how many rounds -  1, 3 or 5?")


def check_player_choice():
    numberOfGames = 0
    validNumberOfGames = False
    while validNumberOfGames == False:
        try:
            numberOfGames = int(input(question))
            if numberOfGames == 1 or numberOfGames == 3 or numberOfGames == 5:
                validNumberOfGames = True
                print(numberOfGames, "Rounds - Let's go!")
            else:
                print("Oops that's not a valid GAME MODE")
        except ValueError:
            print("Oops that's not a valid GAME MODE")
    return numberOfGames

"""if the player selects 1 option run the game once"""
startgame = start()

def play_rounds(numberOfGames):
    i = 1
    while i <= numberOfGames:
        startgame()
        # i += 1
        # print("game")
"""instead of print games make the program call the start function depending on user input"""
        print("game")
        i +=1

play_rounds(3)














