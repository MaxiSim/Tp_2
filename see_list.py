from en_US import ENwords
from es_ES import ESwords

def see_list():
    select = input('What word list do you want to visualize?\n1. English\n2. Español\n> ').lower()
    while select != '1' and select != 'english' and select != '2' and select != 'español':
          select = input('Invalid input, please try again > ')
    if select == '1' or select == 'english':
        for index, word in enumerate(ENwords):
            print (index, word)
    else:
        for index, word in enumerate(ESwords):
            print (index, word)
    
