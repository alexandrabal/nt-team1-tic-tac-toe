import logging

logger = logging.getLogger(__name__)

board_matrix = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


def get_options(board):
    """
    Checks which are the available options.
    :param board: The board configuration
    :return: Array of not-None fields.
    """
    options = []

    for row_index, row_data in enumerate(board):
        for column_index, column_data in enumerate(row_data):
            if column_data is None:
                options.append(row_index * len(board) + column_index + 1)

    return options


def show(board):
    """
    Print the board in console.
    :param board: The board configuration
    """
    print('+---+---+---+')
    logger.info('+---+---+---+')

    for row_index, row_data in enumerate(board):
        row_signs = []
        for column_index, column_data in enumerate(row_data):
            if column_data is None:
                row_signs.append(row_index * len(board) + column_index + 1)
            else:
                row_signs.append(column_data)
        # print('row_signs', row_signs)  # ['x', 2, 'o']
        row_signs = str(row_signs)  # "['x', 2, 'o']"
        row_signs = row_signs.replace('[', '| ').replace(']', ' |').replace(',', ' |').replace("'", '')
        print(row_signs)
        logger.info(row_signs)
        print('+---+---+---+')
        logger.info('+---+---+---+')


def set_choice(board, choice, sign):
    new_board = [x[:] for x in board]

    for row_index, row_data in enumerate(board):
        for column_index, column_data in enumerate(row_data):
            if (row_index * len(board) + column_index + 1) == choice:
                new_board[row_index][column_index] = sign

    return new_board
