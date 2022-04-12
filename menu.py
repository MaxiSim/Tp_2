# -*- coding: utf-8 -*-

from see_list import see_list
from human_hangman import human_hangman
from computer_hangman import computer_hangman
from go_back import go_back


def menu_ppal():
      menu('MENU', list(funciones_menu.keys()))

def play():
    funcplay = menu('Please select a gamemode or go back to the main menu.', list(funciones_menu_play.keys()))
    funciones_menu_play[funcplay]()

def menu(prompt: str, opciones: list) -> str :
    print(prompt)
    for i, opcion in enumerate(opciones):
       print(f'{i + 1}. {opcion}')
  
    return opciones[int(input("> ")) - 1] 
  
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
  
func = menu('MENU', list(funciones_menu.keys()))
funciones_menu[func]()



