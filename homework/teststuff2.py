#!/usr/bin/env python
"""Demonstrates input."""

def AskForThreeWordList():

    while True:
        word_list = raw_input('Please enter exactly 3 words followed by a space or type "q" to quit').islower()
        word_list2 = word_list.split(" ")
        word_list3 = list(word_list2)
        if len(word_list3) != 3:
            print "wtf try again"
        elif len(word_list3) == 3:
            return word_list3
        Convert_To_Pig_Latin()



def RemoveFirstLetter(word):
    word = word.strip(word[0])
    return word

def Convert_To_Pig_Latin():
    words = AskForThreeWordList()
    for word in words:
        if IsVowel(word):
            word += "hay"
            print word
    else:
        for word in words:
            word += "ay"
            print RemoveFirstLetter(word)
            return word

def IsVowel(word):
#    letter = letter.islower()
    if word[0] in 'aeiou':
        return word

AskForThreeWordList()
#Convert_To_Pig_Latin()