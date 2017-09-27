#!/usr/bin/env python
"""Demonstrates input."""

from subprocess import Popen, PIPE
from time import sleep
import os
import sys
os.sys.path.append('/opt/cisco/anyconnect/bin/vpn')

working_directory = '/opt/cisco/anyconnect/bin'

#def LaunchAnyConnect():
#    p = subprocess.call(
#        'printf "AnyConnect-Duo\ndgutierrez\n2usezUDuwUc+\nPUSH\n\n" |/opt/cisco/anyconnect/bin/vpn -s connect vpn.coursehero.com',shell=True)

#def LaunchAnyConnect1():
#    p = Popen(['vpn -s'],stdout=subprocess.PIPE,stdin=subprocess.PIPE),cwd=working_directory)
#            (out, err) = process.communicate('vpn.coursehero.com','AnyConnect-Duo','dgutierrez','2usezUDuwUc+,PUSH')

def LaunchAnyConnect1():
    command = '/opt/cisco/anyconnect/bin/vpn -s'
    p = Popen(['command', '-s'], stdin = PIPE, stdout = PIPE, stderr = PIPE, shell = False)
# issue command
    p.stdin.write(command)
    sleep(0,1)
    while True:
        output = p.stdout.read() # hangs here
        if not output:
            print '[No more data]'
            break
        print output




#        ['vpn', '-s', 'connect', 'vpn.coursehero.com', 'AnyConnect-Duo', 'dgutierrez', '2usezUDuwUc+,PUSH'])
    #p = subprocess.call('printf "AnyConnect-Duo\ndgutierrez\n2usezUDuwUc+\nPUSH\n\n" |/opt/cisco/anyconnect/bin/vpn -s connect vpn.coursehero.com', shell=True)
    subprocess.Popen(['vpn','-s','connect','vpn.coursehero.com','AnyConnect-Duo','dgutierrez','2usezUDuwUc+,PUSH'])
    # print p.communicate()
#'printf "AnyConnect-Duo\ndgutierrez\n2usezUDuwUc+\nPUSH\n\n" |/opt/cisco/anyconnect/bin/vpn -s connect vpn.coursehero.com'


    fw = open("tmpout", "wb")
    fr = open("tmpout", "r")
    p = Popen("./a.out", stdin=PIPE, stdout=fw, stderr=fw, bufsize=1)
    p.stdin.write("1\n")
    out = fr.read()
    p.stdin.write("5\n")
    out = fr.read()
    fw.close()
    fr.close()