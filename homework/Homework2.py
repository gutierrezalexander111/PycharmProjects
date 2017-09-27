"""This program will determine if a single character input is a vowel"""
def AskForSingleLetter():

    while True:
        single_letter = raw_input('Please enter a single letter or type quit to exit : ')
        if not single_letter:
            continue
        elif single_letter == 'quit':
            exit()
            continue
        elif len(single_letter) != 1:
            continue
        else:
            IsVowel(single_letter)
        return single_letter

def IsVowel(letter):
    """This function will figure out if the input by the user is a vowel"""
    if letter not in 'aeiou':
        print "You entered %s this is not a vowel" % letter
        AskForSingleLetter()
    elif letter.isdigit():
        print "You entered %d this is a number not a vowel, try again" % letter
    else:
        print('\033[94m' + 'Awesome! you finally entered %s a vowel' + '\033[94m') % letter
    return letter

def IsLowercaseVowel(letter):
    """This function will determine if the input was in upper case"""
    if  letter.isupper():
        return
def IsUppercaseVowel(letter):
    """This function will determine if the input was in lower case"""
    if  letter.islower():
        return

def PrintIsVowel():
    """This function will print out a message to the user informing the user that their input is a vowel"""
    print IsVowel(AskForSingleLetter())
    return

AskForSingleLetter()