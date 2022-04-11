# -*- coding: utf-8 -*-

from play import play

def menu ()->int:
    '''Selects options from prompt and returns game mode or quit
    '''
    mode = input("MENU\n1. Play\n2. See words list\n3. Quit\nSelect at most one option >").lower()
    while mode != '1' and mode != 'play' and mode != '2' and mode != 'see words list' and mode != '3' and mode != 'quit':
        mode = input('Ingresó un modo inválido, intnte nuevamente > ')
    if  mode == '1' or mode == 'play':
        play()
    elif mode == '2' or mode =='see words list':
        see_list()
    elif mode == 3 or mode == 'quit':
        quit()
