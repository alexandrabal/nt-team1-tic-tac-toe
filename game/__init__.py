from .board import board_matrix as initial_board, get_options, show, set_choice
from .status import check_status
from .player import get_current_player


def start():
    """
    This is the engine of the game.
    """
    is_over = False
    step = 0
    available_options = []
    is_correct_choice = True
    sign = 'x'
    board_matrix = initial_board.copy()

    print('Welcome and good luck!')

    while not is_over:
        if is_correct_choice:
            player_name, sign = get_current_player(step)
            print('%s is your turn.' % player_name)

            available_options = get_options(board_matrix)

        show(board_matrix)
        print('Pick a choice from available options: ', available_options)

        choice = input('Pick your choice: ')
        try:
            choice = int(choice)

            if choice not in available_options:
                raise ValueError()

            is_correct_choice = True
        except ValueError:
            print('Your choice is not an option.')
            is_correct_choice = False
            continue

        board_matrix = set_choice(board_matrix, choice, sign)

        # Check if the game is won or not.
        is_won, is_over = check_status(board_matrix)

        step += 1

    print('Game Over!')
