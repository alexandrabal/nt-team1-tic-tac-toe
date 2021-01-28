def get_current_player(step):
    """
    This function is used for getting data about the current player.
    :param step: Integer about the current iteration.
    :return: (player_name, player_sign)
    """
    if step % 2 == 0:
        name = 'Player 1'
        sign = 'x'
    else:
        name = 'Player 2'
        sign = 'o'

    return name, sign
