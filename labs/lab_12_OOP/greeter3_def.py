#!/usr/bin/env python
"""Alternatively, we define an __init__ method so that the
name is given when the object is created."""
  
class Greeter:
    # This Greeter class needs a name when instantiated.

    def __init__(self, name):
        # __init__ is Python's constructor method
        self.name = name
        print name

    def Greet(self):
        print "Hello World. I'm", self.name

def main():
    fred = Greeter('Fred')
    print fred
    print 'fred.Greet():'
    fred.Greet()

    x = Greeter('shitfaced')    #  error!
    print 'x.Greet():'
    x.Greet()

if __name__ == '__main__':
    main()
