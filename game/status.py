def check_winner(board_matrix):
    """
    Checks if the game is won or not.
    :param board_matrix: Board configuration
    :return: True or False
    """
    return False


def check_status(board_matrix):
    """
    Check if the game is won or is over.
    :param board_matrix: Board configuration
    :return: True or False
    """
    is_won = check_winner(board_matrix)

    if is_won:
        is_over = True
    else:
        is_over = True

        for row in board_matrix:
            if None in row:
                is_over = False
                break

    return is_won, is_over
