from .board import board_matrix as initial_board, get_options, show, set_choice
from .status import check_status
from .player import get_current_player
import logging
import random

logger = logging.getLogger(__name__)


def _found_winning_cell(board_matrix, available_options):
    for choice in available_options:
        check_spots = [x[:] for x in board_matrix]
        new_board = set_choice(check_spots, choice, 'o')
        is_won, _ = check_status(new_board)
        if is_won:
            return True, choice
    return False, None

def _found_blocking_cell(board_matrix, available_options):
    for choice in available_options:
        check_spots = [x[:] for x in board_matrix]
        new_board = set_choice(check_spots, choice, 'x')
        is_won, _ = check_status(new_board)
        if is_won:
            return True, choice
    return False, None

def _check_cell(cell_number, board):
    row = int((cell_number-.5) // 3)
    col = (cell_number - row * 3) - 1
    return board[row][col]

def _computer_move(available_options, board_matrix, last_move, difficulty):
    '''
    difficulties: 'easy' picks randomly from the available options
    'medium' checks to for a winning move for itself, or blocks player from winning on next move. 
    if there is no winning move next move, it chooses a random available option
    'hard' checks for win or blocks player like the medium difficulty, but also strategically picks a move
    if there is no winning or blocking move
    
    return:: choice
    '''
    if difficulty == 'easy':
        choice = random.choice(available_options)
        return choice

    elif difficulty == 'medium':
        found_cell, choice = _found_winning_cell(board_matrix, available_options)
        if found_cell:
            return choice
        found_cell, choice = _found_blocking_cell(board_matrix, available_options)
        if found_cell:
            return choice
        return random.choice(available_options)


    corners = [x for x in available_options if x % 2 == 1 and x != 5]
    winning, choice = _found_winning_cell(board_matrix, available_options)
    if winning:
        return choice
    blocking_needed, choice = _found_blocking_cell(board_matrix, available_options)
    if blocking_needed:
        return choice


    if last_move % 2 == 1 and last_move != 5:
        if 5 in available_options:
            return 5
        opposite_corner = 10 - last_move
        if _check_cell(opposite_corner, board_matrix) == 'x':     
            for choice in available_options:
                if choice % 2 == 0:
                    return choice
    if last_move % 2 == 0:
        if 5 in available_options:
            return 5

    return random.choice(corners)

def _player_move(board_matrix, available_options):
    while True:
        show(board_matrix)
        print('Pick a choice from available options: ', available_options)
        logger.info('Pick a choice from available options: %s' % available_options)

        choice = input('Pick your choice: ')
        logger.info('Pick your choice: ')
        try:
            choice = int(choice)
            if choice not in available_options:
                raise ValueError()
        except ValueError as e:
            print('Your choice is not an option.')
            logger.error('Your choice is not an option.')
            logger.exception(e)
            is_correct_choice = False
            continue
        else:
            is_correct_choice = True
            logger.info('Player choice: %s' % choice)
            return is_correct_choice, choice

def play(cpu=False):
    """
    This is the engine of the game.
    """
    is_over = False
    step = 0
    available_options = []
    is_correct_choice = True
    sign = 'x'
    board_matrix = initial_board.copy()
    winner = None
    player_name = None
    last_move = None
    print('Welcome and good luck!')
    logger.info('Welcome and good luck!')

    while not is_over:
        if is_correct_choice:
            player_name, sign = get_current_player(step, cpu)
            print('%s is your turn.' % player_name)
            logger.info('%s is your turn.' % player_name)

            available_options = get_options(board_matrix)
        if player_name == 'CPU':
            choice = _computer_move(available_options, board_matrix, last_move, cpu)
        else:
            is_correct_choice, choice = _player_move(board_matrix, available_options)


        board_matrix = set_choice(board_matrix, choice, sign)
        last_move = choice

        # Check if the game is won or not.
        is_won, is_over = check_status(board_matrix)

        if is_won:
            winner = player_name
        step += 1

    print('Game Over!')
    logger.info('Game Over!')

    if winner:
        print(f'{winner} has won the game.')
        logger.info(f'{winner} has won the game.')
    else:
        print('Game ended as a draw.')
        logger.info('Game ended as a draw.')