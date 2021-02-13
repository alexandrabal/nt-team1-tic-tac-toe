import sys
from .modes import player_vs_player

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
            player_vs_player()  # call main feature function 
            on_play_menu = False

        elif selection == '2':
            print('Not implemented yet')

        elif selection == '3':
            on_play_menu = False