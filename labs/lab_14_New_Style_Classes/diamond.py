#!/usr/bin/env python
"""
Diamond inheritance in new style classes.
"""
class A(object):
    def __init__(self):
        self.x = 1
class B(A):
    pass
class C(A):
    def __init__(self):
        self.x = 2
class D(B, C):
    pass

print D().x
