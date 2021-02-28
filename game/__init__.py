from .rounds import check_player_choice,play_rounds


def start_play():
    number_of_games = check_player_choice()
    play_rounds(number_of_games)







