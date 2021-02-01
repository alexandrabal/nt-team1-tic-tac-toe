from game.status import check_winner, check_winning_sequence

# board = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# 1, 4, 7 => indexes = [(0, 0), (1, 0), (2, 0)]
# 2, 5, 8 => indexes = [(0, 1), (1, 1), (2, 1)]
# 3, 6, 9 => indexes = [(0, 2), (1, 2), (2, 2)]
# 1, 5, 9 => indexes = [(0, 0), (1, 1), (2, 2)]
# 3, 5, 7 => indexes = [(0, 2), (1, 1), (2, 0)]

# check_winner(board)

boards = [
    [
        ['x', 'x', 'x'],
        ['x', 'o', None],
        [None, None, None]
    ],
    [
        ['x', 'o', 'x'],
        ['o', 'o', 'o'],
        [None, None, None]
    ],
    [
        ['x', 'o', 'x'],
        ['x', 'o', 'x'],
        ['o', 'x', 'x']
    ],
    [
        ['x', 'o', 'x'],
        ['x', 'x', 'o'],
        ['o', 'x', 'x']
    ],
    [
        ['x', 'o', 'o'],
        ['x', 'o', 'o'],
        ['o', 'x', 'x']
    ],
    [
        ['x', 'o', 'x'],
        ['x', 'o', 'o'],
        ['o', 'x', 'x']
    ]
]

for board in boards:
    print(check_winner(board))
