

from en_US import ENwords
from letter_freq import letter_freq



def choose_word(word_list: list)->list:
    word = input('Write the secret word:\n>').lower()
    while word not in word_list:
        word = input('The chosen word is not valid, please choose another one:\n>').lower()
    print('The secret word has been saved!\n\n')
    return list(word)

def find_letter(letter, lst):
    return any(letter in word for word in lst)


def computer_player(word_list: tuple, gameplay_list: list, attempts: list, letter_freq: list):
    possible_words = []
    inword = False
    shift = 0
    for i in word_list:
        if len(i)==len(gameplay_list):
            possible_words.append(i)
    possible_words_copy = possible_words.copy()
    for word in possible_words:
        remover = False
        for e, letter in enumerate(gameplay_list):
            if (letter != '_') and (letter != word[e]):
                remover = True
                break
        for letter in attempts:
            if (letter not in gameplay_list) and (letter in word):
                remover = True
                break
        if remover:
            possible_words_copy.remove(word)
        if len(possible_words_copy)==1:
            return possible_words_copy[0]
    while not inword:
        while letter_freq[len(attempts)+shift] in attempts:
            shift +=1
        for word in possible_words_copy:
            if letter_freq[len(attempts)+shift] in word:
                inword = True
                break
            else:
                continue
        if not inword:
            shift +=1
    return letter_freq[len(attempts)+shift]
    
    

def cmptr_hngmn (word_list: tuple, playgame: bool = True, wingame: bool = False, lives: int = 5):
    print('\n***COMPUTER HANGMAN***\nChoose a secret word and play against the computer')
    secret = choose_word(word_list)
    ingame_list = list('_' * len(secret))
    guessed_list = [] 
    while lives>=1 and wingame == False:
        print (' '.join(ingame_list), f'\n\n{lives} tries remaining  ({" ".join(guessed_list)})\n')
        current_guess = computer_player(ENwords, ingame_list, guessed_list, letter_freq[len(ingame_list)]) 
        if len(current_guess)>1:
            defeat = input(f'Is your word "{current_guess}"? [y/n]>')
            if defeat != 'y':
                print("Don't lie to me!")
            wingame = True
            break
        guessed_list.append(current_guess)
        is_letter_in = input(f'Is the letter "{current_guess}" in the word? [y/n]>').lower()
        while is_letter_in != 'n' and is_letter_in !='y':
            is_letter_in = input('Invalid input, please try again\n>').lower()
        if is_letter_in == 'n':
            lives -=1
        else:
            for i, letter in enumerate(secret):
                if current_guess == letter:
                    ingame_list[i] = current_guess
                    if ingame_list == secret:
                        wingame = True
    if wingame:
        print (f'The computer has won with {lives} lives left! The secret word was "{"".join(secret)}"')
    else:
        print(f'\nThe computer lost! The secret word was "{"".join(secret)}" and the guessed letters were "{", ".join(guessed_list)}"')
    
    
         
