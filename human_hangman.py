# -*- coding: utf-8 -*-

import random 
from en_US import ENwords
from es_ES import ESwords

def human_hangman():
    language = input('Select a language. /nSeleccione un idioma./n1. English/n2. Español/n> ').lower
    
    while language != '1' and language != 'english' and language != '2' and language != 'español':
        language = input('Ingresó un valor inválido, intnte nuevamente. > ')
    
    selected_word = ''
    if language == '1' or language == 'english':
      selected_word = random.choice(ENwords)
    else:
      selected_word = random.choice(ESwords)
      