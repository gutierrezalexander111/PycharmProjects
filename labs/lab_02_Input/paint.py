#!/usr/bin/env python
"""Demonstrates formatted output, and both uses of '%'
1.  string replacement
2.  modulo
"""   
PER_GALLON = 200      # A can of paint covers 200 square feet
sq_ft = 0 
while sq_ft == 0:
    said = raw_input("Number of square feet to paint: ")
    if not said:   # or if said == '':
        print "Thank you anyway." 
        break
    try:
        sq_ft = int(said)
    except ValueError:
        print "Please give a whole number."
else:
    no_cans = sq_ft/PER_GALLON
    if sq_ft % PER_GALLON > 0:
        no_cans += 1
        print "You need %.1f cans so you'd better buy %d %s."\
              % (float(sq_ft)/PER_GALLON, no_cans, 
                 "can" if no_cans==1 else "cans")
    else:
        print "You need exactly %d %s."\
              % (no_cans, "can" if no_cans==1 else "cans")
