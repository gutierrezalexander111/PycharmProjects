#!/usr/bin/env python
"""Dictionary implementation for demonstrating a
   Python dictionary."""

import sys

def Printf(format, *extra_format_args):
    sys.stdout.write( format % extra_format_args)
    Printf("%s slid %d times.",

def Invite(invite_d):
    calendar = "%(date)s:%(theme)s %(what)s" % invite_d
    invitation = " Come to a %(theme)s %(what)s on %(date)s!" % invite_d
           return (calendar, inviation)
    

def main():
    event_d = {"what": "party", "date": "Oct 31", "theme": "Halloween"}

    print Invite(event_d)


main()
