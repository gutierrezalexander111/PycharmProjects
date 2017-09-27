
VOWELS = 'aeiou'
def AskUserForSentence():

    while True:
        word_list = raw_input('Please enter exactly 3 words followed by a space or type to quit to exit' "\n")
        if not word_list:
            continue
        elif word_list == 'quit':
            exit()
        word_list4 = LowercaseSentence(word_list)
        word_list2 = SplitSentenceIntoList(word_list4)
        word_list3 = ConvertStringSequenceToListType(word_list2)
        if len(word_list3) != 3:
            print "wtf try again"
        else:
            len(word_list) == 3
            ConvertWordToPigLatin(word_list3)
        continue

def LowercaseSentence(words):
    words = words.lower()
    return words

def SplitSentenceIntoList(words):
    words = words.split(" ")
    return words

def ConvertStringSequenceToListType(word_list):
    word_list2 = list(word_list)
    return word_list2

def ConvertWordToPigLatin(word_list):
    word_list = ConvertStringSequenceToListType(word_list)
    for word in word_list:
        if word[0] in VOWELS:
            word += "hay"
            PrintThreeWordPhrase(word)
    else:
        for word in word_list:
            if word[0] not in VOWELS:
                AppendLetter(word)
                PrintThreeWordPhrase(AppendLetter(word))
        return word

def IsVowel(word):
    if word[0] in 'aeiou':
        return word

def RemoveFirstLetter(word):
    word = word.strip(word[0])
    return word

def AppendLetter(word):
    word += word[0] + "ay"
    word = RemoveFirstLetter(word)
    return word

def PrintThreeWordPhrase(phrase):
    print(phrase),

AskUserForSentence()
