#!/usr/bin/env python
"""(Optional) Function to generate random numbers without 
repetition.  Demonstrates generators and the 'yield' keyword."""
import random 

def GiveFew():
    yield 1
    yield 2
    yield 3

def Unique(bot, over_top):
    """Generator to deliver randomly chosen values from bot
    to over_top - 1, delivering each value once only."""
    answers = range(bot, over_top)
    random.shuffle(answers)
    for each in answers:
        yield each

def ListUnique(bot, over_top):
    """Returns a list of the generated numbers
    """
    gen = Unique(bot, over_top)
    while True:
        try:
            print gen.next(),
        except StopIteration:
            return

def ListUnique(bot, over_top):
    """Same action!
    """
    for number in Unique(bot, over_top):
        print number,
    print

if __name__ == '__main__':
    for number in GiveFew():
        print number,
    print
    print 'ListUnique(10, 21) --> ',
    ListUnique(10, 21)
