# -*- coding: utf-8 -*-

from see_list import see_list
from human_hangman import human_hangman
from computer_hangman import computer_hangman

def go_back():
      '''
      Goes back to the main menu.s
      '''
      call()

def menu_ppal():
      '''
      Calls menu() with the parameters of the main menu.
      --Arguments--
      str            -> the name that displays with the menu.
      funciones_menu -> dictionary with the options for the menu. 
      '''
      menu('MENU', list(funciones_menu.keys()))

def play():
      '''
      Calls menu() with the parameters for the Play mode menu.
      --Arguments--
      str                 -> text that displays with the menu.
      funciones_menu_play -> dictionary with the options for the menu. 
      '''
      funcplay = menu('Please select a gamemode or go back to the main menu.', list(funciones_menu_play.keys()))
      funciones_menu_play[funcplay]()

def menu(prompt: str, opciones: list) -> str :
      while True:   
         print(prompt)
         for i, opcion in enumerate(opciones):
            print(f'{i + 1}. {opcion}')
         selected = int(input('> '))
         if selected != 1 and selected != 2 and selected != 3:
            print('That is not a valid option. Try again.')
            continue
         else:    
            return opciones[selected - 1]

def call():
      '''
      Only when called by main.py, the file is executed. 
      '''
      func = menu('MENU', list(funciones_menu.keys()))
      funciones_menu[func]()
    
funciones_menu = {
  'Play': play,
  'See list': see_list, 
  'Quit': quit
}            
funciones_menu_play = {
  'Human Hangman': human_hangman,
  'Computer Hangman': computer_hangman,
  'Go Back': go_back
}





