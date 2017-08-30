#!/usr/bin/env python
"""Write a DoBreakfast function that takes five arguments:
meat, eggs, potatoes, toast, and beverage.  The default
meat is bacon, eggs are over easy, potatoes is hash browns,
toast is white, and beverage is coffee.

The function prints:

Here is your bacon and scrambled eggs with home fries
and rye toast.  Can I bring you more milk?

Call it at least 3 different times, scrambling the arguments.
"""

def DoBreakfast(meat="bacon", eggs="over easy", 
              potatoes="hash browns", toast="white", 
              beverage="coffee"):
    print "Here is your %s and %s eggs with %s and %s toast." % (
        meat, eggs, potatoes, toast)
    print "Can I bring you more %s?" % beverage

def main():
    DoBreakfast()
    DoBreakfast("ham", "basted", "cottage cheese",
                "cinnamon", "orange juice")
    DoBreakfast("sausage", beverage="chai", toast="wheat")

main()
