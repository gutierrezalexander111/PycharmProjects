#!/usr/bin/env python


import keyring
import subprocess

# setup these variables

#VPNGROUP = ''  # The VPN group you are trying to connect to (numerical)
USERNAME = 'dgutierrez'  # This is the username for the vpn connection
SYSNAME = 'AnyConnect'  # This is the name of the entry in Keychain that stores your credentials
COMMAND = '/opt/cisco/anyconnect/bin/vpn'
OPTION1 = '-s' # argument to vpn binary
OPTION2 = 'connect' # argument to vpn binary
HOST = 'vpn.coursehero.com' #The hostname or IP of the VPN device you are trying to connect to
password = keyring.get_password(SYSNAME,USERNAME).encode('ascii')

#try:
#    import keyring
#except ImportError:
#    sys.stderr.write(
#        "You do not have 'keyring' installed.  Please see https://pypi.python.org/pypi/keyring for more information.")
#    exit(1)

#def GetPassword(SYSNAME,USERNAME):
#    keyring.get_password(SYSNAME,USERNAME).encode('ascii')
#    return

cmdline = [COMMAND, OPTION1, OPTION2, HOST]
cmd = subprocess.Popen(cmdline, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
cmd.stdin.write('1\n\n')
#cmd.stdin.write('2usezUDuwUc+\n')
print cmd.stdin.write(str('%s\n' % password))
cmd.stdin.write('PUSH\n\n')
for line in iter(cmd.stdout.readline,""):
    print line

#def launchGUI():
#    os.system('open -a "Cisco AnyConnect Secure Mobility Client"')

#def main():
    #password = GetPassword(SYSNAME,USERNAME).encode('ascii')
#    launchGUI()
#    print password
#    if __name__ == '__main__':
#       main()