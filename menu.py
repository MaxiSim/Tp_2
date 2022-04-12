# -*- coding: utf-8 -*-

from see_list import see_list

def menu ():
    '''Selects options from prompt and returns game mode or quit
    '''
    run = True
    while run:
        mode = input("MENU\n1. Play\n2. See words list\n3. Quit\nSelect one option > ").lower()
        while mode != '1' and mode != 'play' and mode != '2' and mode != 'see words list' and mode != '3' and mode != 'quit':
            mode = input('Ingresó un modo inválido, intnte nuevamente > ')
        if  mode == '1' or mode == 'play':
            play()
        elif mode == '2' or mode =='see words list':
            see_list()
            continue
        elif mode == '3' or mode == 'quit':
            run = False

def play():
  select_option = input('''Please select an option to continue:\n1. Human Hangman\n2. Computer Hangman\n3. Go Back\n>''').lower()

  while select_option != '1' and select_option != 'human hangman' and select_option != '2' and select_option != 'computer hangman' and select_option != '3' and select_option != 'go back':
        select_option = input('Invalid input, please try again > ')
        
  if select_option == '1' or select_option == 'human hangman':
    print('human')
    #human_hangman()
  elif select_option == '2' or select_option == 'computer hangman':
    print('computer')
    #computer_hangman()
  else:
    menu()
    #go_back()

