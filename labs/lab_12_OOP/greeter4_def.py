#!/usr/bin/env python
"""Here we implement 'inheritance' to leave the original
Greeter class intact and add a NamedGreeter class, that
has all the functionality of the Greeter class plus some
new things. """

class Greeter: 

    def Greet(self):
        print "Hello World"

class NamedGreeter(Greeter):
    # Inherits the methods in the Greeter class, and adds some
    # of its own-remember fred is a namespace object instance like Gracy was do fred.Greet means the namespace fred object instance of Greeter can do Greet method which is to say hello.

    def __init__(self, name):
        self.name = name

    def SayMyName(self):
        print "I'm", self.name

def main():
    fred = NamedGreeter('Fred')
    print 'fred.Greet():'
    fred.Greet()
    fred.SayMyName()

    # code that depends on the Greeter class is unaffected. this shows the the Greeter class is not changes it is a class not an object
    x = Greeter()
    print 'x.Greet():'
    x.Greet()

if __name__ == '__main__':
    main()
