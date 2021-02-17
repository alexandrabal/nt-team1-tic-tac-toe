def get_current_player(step, cpu):
    """
    This function is used for getting data about the current player.
    :param step: Integer about the current iteration.
    :return: (player_name, player_sign)
    """
    if step % 2 == 0:
        name = 'Player 1'
        sign = 'x'
    else:
        if not cpu:
            name = 'Player 2'
        else:
            name = 'CPU'
        sign = 'o'

    return name, sign
