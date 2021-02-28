from copy import deepcopy

def check_winning_sequence(sequence):
    """
    Checks for winning sequence.
    :param sequence: The sequence of signs to check
    :return: True/False
    """
    sequence_set = set(sequence)
    return len(sequence_set) == 1 and None not in sequence_set

def check_winner(board_matrix):
    """
    Checks if the game is won or not.
    :param board_matrix: Board configuration
    :return: True or False
    """
    is_won = False

    for sequence in board_matrix:
        is_won = check_winning_sequence(sequence)
        deepcopy(board_matrix)
        if is_won:
            return True

    for column_index in range(len(board_matrix)):  # column_index => [0, 2]
        sequence = []
        for row_index in range(len(board_matrix)):  # row_index => [0, 2]
            sequence.append(board_matrix[row_index][column_index])

        is_won = check_winning_sequence(sequence)

        if is_won:
            return True

    sequence = []
    for index in range(len(board_matrix)):
        sequence.append(board_matrix[index][index])
    is_won = check_winning_sequence(sequence)

    if not is_won:
        sequence = []
        for index in range(len(board_matrix)):
            first_index = index
            second_index = len(board_matrix) - index - 1
            sequence.append(board_matrix[first_index][second_index])
        is_won = check_winning_sequence(sequence)

    return is_won

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
