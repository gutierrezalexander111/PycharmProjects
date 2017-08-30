#!/usr/bin/env python
"""Processing team data using exec and eval."""
import sys
def NotifyForwards(): 
    return "Go for the goal!" 
def NotifyDefenders():
    return "Block that kick!"
def NotifyMidfielders():
    return "Get that ball!"
def NotifyGoalies():
    return "Guard the goal!"

def ProcessTeam(stream):
    positions = []
    for line in stream:
        line = line.strip()
        if not line:
            continue
        if line.endswith(':'):
            position = line[:-1]
            exec "%s = []" % (position) in globals()
            positions += [position]
            continue
        details = line.split(' ', 1)
        exec "%s += [details]" % (position)
        exec "print 'Yeh %s #%s ' + Notify%s()" %\
        (details[1], details[0], position)
    return stream.name, positions

def PrintTeam(team_name, positions):
    print '\n%s:' % team_name 
    for each in positions:
        print '  %s:' % each
        for player in sorted(eval(each)):
            print '    ' + ': '.join(player)

def main(team_name = "Bees"):
    team_name, positions = ProcessTeam(open(team_name))
    PrintTeam(team_name, positions)
    print "\nThe %s data file:" % (team_name)
    sys.stdout.write(open(team_name).read())

main()
