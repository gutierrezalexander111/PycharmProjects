#!/usr/bin/env python
"""function_nest.py Adapted from 'Learning Python'
by Mark Lutz & Davis Ascher"""  

x = 11
def F1():
    x = 99           # <- Visible in the nest but not outside
    def F2():
        def F3():
            print x  # <- Can see outside namespaces
            y = 4    # <- Not visible from outside.
        F3()
    F2()

if __name__ == '__main__':
    F1()
