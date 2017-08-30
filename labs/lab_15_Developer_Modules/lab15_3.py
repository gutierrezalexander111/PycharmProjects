#!/usr/bin/env python
"""lab15_3.py Make a TimeOut context handler so that this 
code works.""" 
    
import signal, time 

class TimeOut:

    def __init__(self, timeout):
        self.timeout = timeout

    def __enter__(self):
        def AlarmHandler(signum, frame):
            raise RuntimeError, \
                  "Timed out after %s seconds."\
                  % (self.timeout)
        self.old = signal.signal(signal.SIGALRM, AlarmHandler)
        signal.alarm(self.timeout)
        return True

    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.signal(signal.SIGALRM, self.old)
        signal.alarm(0)

with TimeOut(2) as ticker:
    try:
       time.sleep(5)
    except RuntimeError, info:
       print "Sleeping 5 timed out!", info

with TimeOut(5) as ticker:
    try:
       time.sleep(2)
       print "Sleeping 2 didn't time out."
    except RuntimeError:
       print "Timed out!"
