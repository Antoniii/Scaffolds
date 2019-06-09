#!/usr/bin/python3
'''
       __       __  
      | _|     |_ |        ___       _  _               
      | |   _   | |       / __| ___ (_)| | ___  _ _  ___
      | |  (_)  | |      | (__ / -_)| || |/ _ \| '_|(_-<
      | |       | |       \___|\___||_||_|\___/|_|  /__/                               
      |_|       |_| 


                    HANGMAN REVENGE v0.666
                     --= TONY EDITION =--


                      ***  CREDITS: ***

                 ORIGINAL AUTHOR: Tony Adams
                    ART DIRECTOR: Alex Courlyck
                  HEAD DEVELOPER: Eli Stepper
                    CODE STYLER,
                  LEAD DEVELOPER: Johnny Abdrams

                     (c) Ceilors, 2k19

'''

import random
import re
from typing import Set

regex = re.compile('^[а-я]$')
stages = [
    '________        ',
    '|        |      ',
    '|        |      ',
    '|        |      ',
    '|        |      ',
    '|        0      ',
    '|       /|\     ',
    '|       / \     ',
    '|               '
]


def mask_word(word: str, masked_letters: Set[str]) -> str:
    '''

    Parameters
    ----------

        word : str
            word needs to be masked

        masked_letters : Set[str]
            letters should be masked

    Returns
    -------

        masked word : str
    '''
    return ''.join(['_' if c in masked_letters else c for c in list(word)])


def hangman(word: str):
    word = word.lower()
    wrong_guesses = set()
    remaining_letters = set(list(word))
    win = False
    print('Добро пожаловать на казнь русских слов!')
    while len(wrong_guesses) < len(stages):
        guess = input('Введите букву: ').lower()
        if not regex.match(guess):
            print("Используй русские буквы")
            continue
        print('')
        if guess in remaining_letters:
            remaining_letters.discard(guess)
        else:
            wrong_guesses.add(guess)

        if wrong_guesses:
            print(f'Неудачные попытки: {" ".join(wrong_guesses)}')

        print(mask_word(word, remaining_letters))
        print('\n'.join(stages[:len(wrong_guesses)]))

        if not remaining_letters:
            win = True
            break
    if not win:
        print('\n'.join(stages))
        print(f'Вы проиграли! Было загадано слово: {word}')
    else:
        print(f'Вы выиграли! Было загадано слово: {word}')


if __name__ == '__main__':
    with open('word_rus.txt') as f:
        words = f.readlines()
        hangman(random.choice(words).strip())
