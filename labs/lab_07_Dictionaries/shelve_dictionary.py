#!/usr/bin/env python
"""shelve_dictionary.py
Now, we are making the dictionary persistent by 'shelving' it.
"""
import shelve 
from py_dict_def import *

def main():
    try:
        py_dict = shelve.open("py_dict.dat")
    except IOError:
        print 'File could not be opened.'
        return

    RunMenu(py_dict)

    py_dict.close()

if __name__ == '__main__':
    main()
