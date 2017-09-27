


def AskForThreeWordList():

    while True:
        word_list = raw_input('Please enter exactly 3 words followed by a space or type to quit to exit')
        if not word_list:
            continue
        elif word_list == 'quit':
            exit()
        word_list2 = MakeStringSeguenceFromWords(word_list)
        word_list3 = ConvertStringSequenceToListType(word_list2)
        if len(word_list3) != 3:
            print "wtf try again"
        else:
            len(word_list) == 3
            Convert_To_Pig_Latin(word_list3)
        return word_list3
        break

def MakeStringSeguenceFromWords(words):
    words = words.split(" ")
    return words

def ConvertStringSequenceToListType(word_list):
    word_list2 = list(word_list)
    return word_list2

def Convert_To_Pig_Latin(word_list):
    word_list = ConvertStringSequenceToListType(word_list)
    for word in word_list:
        if word[0] in 'aeiou':
            word += "hay"
            print word
        else:
            AppendLetter(word)
def IsVowel(word):
    if word[0] in 'aeiou':
        return word

def RemoveFirstLetter(word):
    word = word.strip(word[0])
    return word

def AppendLetter(word):
    word += word[0] + "ay"
    word = RemoveFirstLetter(word)
    print word
    return word

AskForThreeWordList()