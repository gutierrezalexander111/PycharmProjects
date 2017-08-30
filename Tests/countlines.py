#!/usr/bin/python
def CountVowels(my_string):
    my_string= my_string.lower()
    count=0
    for vowel in 'aeiou':
        count += my_string.count(vowel)
    return count

if __name__== '__main__':
    
    print CountVowels('Intuit')
    
