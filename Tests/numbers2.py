#!/usr/bin/python
my_user_string = raw_input('Please type is a number for your ordered list')
def main():
    i = 0
    numbers = []
    try:
        number = int(my_user_string)
    except ValueError:
        print "This is not a number dude"
    while i < number:
        print "At the top i is %d"%i
        numbers.append(i)
        i = i + 1
        print "Numbers now:", numbers
        print "At the bottom i is %d" %i
        print "The numbers:"

    for num in numbers:
        print num

main()
        
