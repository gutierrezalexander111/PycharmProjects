#!/usr/bin/env python
"""Here we have a NamedGreeterGuru Class, and a
GuruNamedGreeter Class, overriding the Bye()
method in the Guru class, demonstrating left-
right, depth-first method resolution.
"""
import random 
    
class Guru:    
    # And here is a class attribute, accessable anywhere
    # by Guru.sayings  
    sayings = ("There is no solution, for there is no"
               "\nproblem.               Marcel Duchamp", 
               "If you could get rid of yourself just once,"
               "\nThe secret of secrets would open to you."
               "\n                            Jalaluddin Rumi", 
               "Nothing is so simple that it cannot be"
               "\nmisunderstood.          Freeman Teague", 
               "What one understands is only half true."  
               "\nWhat one does not understand is the full"
               "\ntruth.                        Zen Saying", 
               "Trying to define yourself is like trying"
               "\nto bite your own teeth.       Alan Watts")

    def Bye(self):
        print "Good Bye.  And remember:"
        self.Pontificate()

    def Pontificate(self):
        print random.choice(Guru.sayings)

class Greeter:

    def Greet(self):
        print "Hello World"

    def Bye(self):
        print "Bye now."

class NamedGreeter(Greeter):

    def __init__(self, name):
        self.name = name

    def Greet(self):
        Greeter.Greet(self)
        print "I'm", self.name

class GuruNamedGreeter(Guru, NamedGreeter):
    pass

class NamedGreeterGuru(NamedGreeter, Guru):
    pass

def main():
    rocky = GuruNamedGreeter("Rocky")
    rocky.Greet()
    rocky.Pontificate()
    rocky.Bye()

    moose = NamedGreeterGuru("Moose")
    moose.Greet()
    moose.Pontificate()
    moose.Bye()
    print "\nAccessing the class attribute:"
    print random.choice(Guru.sayings)

if __name__ == '__main__':
    main()
