#!/usr/bin/env python 
"""lab10_3.py
Finds and reports the OS and IP address of this machine.
"""
import subprocess
import sys

def GetLinuxIP():
    """Returns the IP address for Linux machines."""

    output = subprocess.Popen("/sbin/ifconfig",
                              stdout=subprocess.PIPE).stdout
    for line in output:
        address_at = line.find("inet addr:")
        if address_at == -1:
            continue
        return line[address_at + 10:].split()[0]

def GetWindowsIP():
    """Returns the IP address for Windows machines."""

    popen_obj = subprocess.Popen(
        ("c:\windows\system32\ipconfig.exe", "/all"),
        stdout=subprocess.PIPE)
    output = popen_obj.stdout
    for line in output:
        address_at = line.find("IPv4 Address")
        if address_at == -1:
            continue
        ip_address = line.split()[-1]
        if ip_address[-1] == ')':
            ip_address = ip_address[:ip_address.index('(')]
        return ip_address

def main():                          
    this_os = sys.platform            
    print this_os                     
    if this_os.find("win") > -1:      ################
        print GetWindowsIP()          #  OUTPUT
    elif this_os.find("linux") > -1:  #  $ lab10_3.py
        print GetLinuxIP()            #  win32
    else:                             #  192.168.1.108
        print "Unknown OS"            #
                                      #  $ lab10_3.py
if __name__ == '__main__':            #  linux2
    main()                            #  192.168.1.109
