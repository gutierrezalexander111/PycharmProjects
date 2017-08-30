#!/usr/bin/env python 
"""prof.py Demonstrates the profiler which spits out info 
about the time it takes to run functions.""" 
import cProfile

__pychecker__ = 'no-local' 
LIMIT = 12   
data = range(LIMIT)

def TryWay(index):
    """Uses try/except to return data or None.f
    """
    try:
        return data[index]
    except:
        return None

def TestWay(index):
    """Tests the index to return None if there is no
    data for the index.
    """
    if index < -len(data) or index > len(data) - 1:
        return None
    return data[index]

def TestWay2(index):
    """Checks the i (index) against the len(data) to 
    determine if there is no data.
    """
    data_len = len(data)
    if index < -data_len or index > data_len - 1:
        return None
    return data[index]

def TestPercentWrong(times, percent_wrong):
    """Tests the three functions with the a certain
    percent of failures. """
    print "Testing %d%% wrong." % (percent_wrong)
    cycle_at = 100. * LIMIT/(100 - percent_wrong)
    if cycle_at != round(cycle_at, 0):
        raise ValueError, (
              "Inputs will not produce a fair comparison.")
    cycle_at = int(cycle_at)
    # pychecker complains that i is unused below! 
    for i, j in enumerate(range(times)): 
        j %= cycle_at
        TryWay(j)
        TestWay(j)
        TestWay2(j)

if __name__ == '__main__':
    for percent in (25, 50):
        cProfile.run("TestPercentWrong(%d, %d)" % (
            10000, percent))
