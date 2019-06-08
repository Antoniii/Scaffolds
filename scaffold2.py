#!/usr/bin/python2
# -*- encoding: utf-8 -*-
import random
import urllib2

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib2.urlopen(word_site)
txt = response.read()
WORDS = txt.splitlines()

word_list = len(WORDS)
random_number = random.randint(0, word_list)


def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print "Добро пожаловать на казнь английских слов!"
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = raw_input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print " ".join(board)
        e = wrong + 1
        print "\n".join(stages[0: e])
        if "__" not in board:
            print "Вы выиграли! Было загадано слово: "
            print " ".join(board)
            win = True
            break
    if not win:
        print "\n".join(stages[0: wrong])
        print "Вы проиграли! Было загадано слово: {}.".format(word)

#print WORDS[random_number]
hangman(WORDS[random_number])
