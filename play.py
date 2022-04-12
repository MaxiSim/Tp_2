
from menu import menu

def play():
  select_option = input('''Please select an option to continue:
                           1. Human Hangman
                           2. Computer Hangman
                           3. Go Back

                           >''').lower()

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

