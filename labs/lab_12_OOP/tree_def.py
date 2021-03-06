#!/usr/bin/env python
"""
A Tree class, to make tree objects, and a Forest class.
The Forest class is a "container" class because it 
contains the tree objects.

In UML (Unified Modeling Language), this container 
relationship, which is very common, is pictured:

            --------
           |        |
           | Forest |
           |        |
            --------
             / \
             \ /  A diamond means "has a".
              |   Forest has a Tree.
            --------
           |        |
           |  Tree  |
           |        |
            --------

"""
import random 

class Tree:
    """Instantiate:  Tree(20) to make a tree 20 ft tall.
    """
    def __init__(self, height):
        self.height = height

    def Print(self):
        print "tree, %.1f feet tall" % (self.height)

class Forest:
    """Instantiate: Forest(size='medium')
    if size == 'large', it will have 8 trees.
            == 'medium', it will have 5 trees.
            == 'small', it will have 2 trees.
    """
    def __init__(self, size='medium'):
        if size not in ("small", "medium", "large"):
            raise ValueError, """Intantiate with: 
Forest([size='medium']) where size can be 'small', 'medium', 
or 'large', not '%s'.""" % size
        self.size = size
        self.number_of_trees = 8 if self.size == 'large' \
		  else 5 if self.size == 'medium' else 2
        self.trees = [Tree(random.randrange(1,200)) 
                      for count in range(self.number_of_trees)]

    def Print(self):
        print "%s forest with %d trees:" % (self.size, 
                                            self.number_of_trees)
        for tree in self.trees:
            tree.Print()
        print

def main():
    for size in 'small', 'medium', 'large':
        forest = Forest(size)
        forest.Print()
    try:
        forest = Forest('huge')
    except ValueError, info:
        print info

if __name__ == '__main__':
    main()
