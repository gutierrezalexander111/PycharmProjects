#string = range(1,4)
#string_2 = "CONTACT"
#string.reverse()
#string_3 = list(string_2)
#print string[0], string[1], string[2], string_2
#print string_3
#string.reverse()
#print string
#string += string_3
#print string
#string_2.split("CONTACT")
#string_2[:]
#print string_2
#string += string_2
#print string
#print string
#print string, "CONTACT"
#print string[0], string[1], string[2]


#"""Write a program that takes a 3 word phrase and then converts the words to Pig Latin."""

def AppendLetter(word):
    word = join.(word.append(word[0])."ay"
    print word

AppendLetter(["BOY"])


def AskForThreeWordList():

    while True:
        word_list = raw_input('Please enter exactly 3 words followed by a space or type to quit to exit')
        if not word_list:
            continue
        elif word_list == 'quit':
            exit()
        word_list4 = LowercaseSentence(word_list)
        word_list2 = MakeStringSeguenceFromWords(word_list4)
        word_list3 = ConvertStringSequenceToListType(word_list2)
        if len(word_list3) != 3:
            print "wtf try again"
        else:
            len(word_list) == 3
            Convert_To_Pig_Latin(word_list3)
 #      return word_list3
        break

def LowercaseSentence(words):
    words = words.lower()
    return words

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
            PrintThreeWordPhrase(word)
        else:
            print AppendLetter(word)
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
    print(phrase)

AskForThreeWordList()