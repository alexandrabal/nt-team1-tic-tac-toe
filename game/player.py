import random

silly_names = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
               "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
               'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
               'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
               'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
               'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
               'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
               'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid',
               '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
               'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
               'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
               "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
               'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
               'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
               "Winston 'Jazz Hands'", 'Worms')


def get_current_player(step):
    """
    This function is used for getting data about the current player.
    :param step: Integer about the current iteration.
    :return: (player_name, player_sign)
    """
    if step % 2 == 0:
        # name = 'Player 1'
        name = players['player1']['first name'] + ' ' + players['player1']['last name']
        sign = 'x'
    else:
        # name = 'Player 2'
        name = players['player2']['first name'] + ' ' + players['player2']['last name']
        sign = 'o'

    return name, sign


players = {}


def ask_player_names():
    """
    This function is used for greeting users and for getting their first and last names.
    If input not provided, then select random from list of silly names.
    Finally, appends player's names to dict players.
    return: dict of {'first name': 'input', 'last name': 'input'}
    """
    prompt = [
        ['intro', 'Welcome to the games of Tic-Tac-Toe!'],
        ['first name', 'What\'s your first name?\n'],
        ['last name', 'What\'s your last name?\n'],
    ]
    print(prompt[0][1])  # print intro: Greet player
    # get list of answers, exclude intro
    answers = [input(prompt[x][1]).strip() for x in range(1, len(prompt))]
    # validate input: check for blanks, ask again, else assign random wacky name
    for x, y in enumerate(answers):
        if answers[x] == '':
            answers.pop(x)
            temp = input(f'You can\'t ghost out on this. Please insert your {prompt[x + 1][0]} '
                         f'or we\'ll give you a silly one!\n')
            temp = random.choice(silly_names) if temp.isspace() else temp
            answers.insert(x, temp)
    # reconstruct answers:
    # 1. zip prompt list elements position 0 (e.g. 'first name') with answers list
    # 2. create dict
    answers = dict(zip([prompt[x][0] for x, y in enumerate(prompt) if prompt[x][0] != 'intro'], answers))
    # test if dict is empty (passing an empty string returns a False, as failure to convert something that is empty)
    if not bool(players):
        players['player1'] = answers
    else:
        players['player2'] = answers
    # return answers
