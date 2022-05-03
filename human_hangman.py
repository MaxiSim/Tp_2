# -*- coding: utf-8 -*-

import random
from en_US import ENwords


def random_word():
      '''
      -- Asks the user to select a language and randomly selects a word from that dictionary.
      -- Returns the random word as a list; a list with the same amount of '_' as letters of the random word; the language that the user selected;
      the random word as a string.
      
      --Arguments--
      language        -> input: the user selects a language for the word.
      selected_word   -> variable, str: saves the generated word. 
      new_word        -> variable, list: saves the generated word letter by letter as a list.
      dash_word_list  -> variable, list: saves a list of '_' with the length of the random word. 
      '''

      selected_word = random.choice(ENwords)
      new_word = []
      dash_word_list = []
      for letter in selected_word:
            new_word += letter
            
      for letter in range(len(new_word)):
            dash_word_list += '_' 
            
  

      return new_word, dash_word_list, selected_word
  
def human_hangman():
      '''
      -- Runs the code in which the user plays the game. Asks the user to guess the letters or word that the program generated. 
      -- Returns a message if the player wins or looses.
       
      --Arguments--
      left_tries      -> variable, int: starts at 5 and is reduced as the player fails to guess a letter. 
      used_letters    -> variable, list: saves the letters that the user entered in the input.
      guess_letter    -> variable, str: saves the letter entered each time by the user. 
      --Arguments from random_word() function--
      language        -> input: the user selects a language for the word.
      selected_word   -> variable, str: saves the generated word. 
      new_word        -> variable, list: saves the generated word letter by letter as a list.
      dash_word_list  -> variable, list: saves a list of '_' with the length of the random word.  
      '''
      new_word, dash_word_list, selected_word = random_word()
      left_tries = 5
      used_letters = []
      
      while True:
        print('')
        print('You have, ', (left_tries), 'tries left.')
        print(' '.join(dash_word_list), (used_letters))
        guess_letter = input('Enter a letter or word: > ').lower()
        
        if len(guess_letter) == 1:
          if guess_letter in new_word:
              for i in range(len(new_word)):
                if guess_letter == new_word[i]:
                  dash_word_list[i] = guess_letter
                  
                  if guess_letter not in used_letters:
                    used_letters += guess_letter
                    
          elif guess_letter not in new_word:
            left_tries -= 1
            used_letters += guess_letter
            if left_tries >0:  
              continue
            elif left_tries == 0:
              print(f'GAME OVER\nThe word was {selected_word}')
              return False
            
        elif len(guess_letter)>1:
            if guess_letter == selected_word:
              print(f'YOU WON')
              return False
            else:
              print(f'GAME OVER\nThe word was {selected_word}')
              return False
            
        if dash_word_list == new_word :
          print(f'YOU WON')
          return False
        
