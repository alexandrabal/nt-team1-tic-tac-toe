import sys
from .gamemodes import player_vs_player

def main_menu():
    '''
    Displays main menu options
 
    '''
    print('\nMain Menu')
    print('----------')
    print('1. Play')                    # play submenu function created below
    print('2. Exit')                    # add more print lines for other submenus
                                        
    on_main_menu = True
    while on_main_menu:     
        selection = input('>: ')
        if selection == '1':            # add an if check for the new menu added
            on_main_menu = False
            print('Selected Play')
            play_menu()                 # call menu or feature function
        elif selection == '2':
            print('exiting')
            sys.exit()


def play_menu():
    '''
    Displays play menu options

    '''
    print('\nPlay')
    print('----------')
    print('1. Vs Player')
    print('2. Vs Computer')
    print('3. Return to Main Menu')
    on_play_menu = True
    while on_play_menu:
        selection = input('>: ')
        if selection == '1':
            on_play_menu = False
            player_vs_player()                      # call main feature function 

        elif selection == '2':
            print('Not implemented yet')

        elif selection == '3':
            on_play_menu = False
            main_menu()