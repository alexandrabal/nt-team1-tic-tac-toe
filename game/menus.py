from .modes import play

def main_menu():
    '''
    Displays main menu options
    '''                                       
    while True:     
        print('\nMain Menu')
        print('----------')
        print('1. Play')  # play submenu function created below
        print('2. Exit')  # add more print lines for other submenus
        
        selection = input('>: ')
        if selection == '1':  # add an if check for the new menu added
            print('Selected Play')
            play_menu()  # call menu or feature function
        elif selection == '2':
            break

def play_menu():
    '''
    Displays play menu options
    '''
    on_play_menu = True   
    while on_play_menu:
        print('\nPlay')
        print('----------')
        print('1. Vs Player')
        print('2. Vs Computer')
        print('3. Return to Main Menu')
        
        selection = input('>: ')
        if selection == '1':
            play()  
            on_play_menu = False

        elif selection == '2':
            select_difficulty_menu()
            on_play_menu = False

        elif selection == '3':
            on_play_menu = False

def select_difficulty_menu():
    '''
    Displays CPU difficulties to choose from
    '''
    on_difficulty_menu = True
    while on_difficulty_menu:
        print('\nChoose difficulty')
        print('----------')
        print('1. Easy')
        print('2. Medium')
        print('3. Hard')

        selection = input('>: ')
        if selection == '1':
            play(cpu='easy')
            on_difficulty_menu = False

        elif selection == '2':
            play(cpu='medium')
            on_difficulty_menu = False

        elif selection == '3':
            play(cpu='hard')
            on_difficulty_menu = False
