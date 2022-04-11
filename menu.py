# -*- coding: utf-8 -*-


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

def play():
  select_option = input('''Please select an option to continue:\n1. Human Hangman\n2. Computer Hangman\n3. Go Back\n>''').lower()

  while select_option != '1' and select_option != 'human hangman' and select_option != '2' and select_option != 'computer hangman' and select_option != '3' and select_option != 'goback':
        select_option = input('Ingresó un modo inválido, intnte nuevamente > ')
        
  if select_option == '1' or select_option == 'human hangman':
    print('human')
    #human_hangman()
  elif select_option == '2' or select_option == 'computer hangman':
    print('computer')
    #computer_hangman()
  elif select_option == '3' or select_option == 'go back':
    menu()
    #go_back()

