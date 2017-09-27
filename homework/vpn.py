
import keyring
import subprocess

# setup these variables

#VPNGROUP = ''  # The VPN group you are trying to connect to (numerical)
USERNAME = 'dgutierrez'  # This is the username for the vpn connection
SYSNAME = 'AnyConnect'  # This is the name of the entry in Keychain that stores your credentials
COMMAND = '/opt/cisco/anyconnect/bin/vpn'
OPTION1 = '-s'
OPTION2 = 'connect'
HOST = 'vpn.coursehero.com' #The hostname or IP of the VPN device you are trying to connect to
password = keyring.get_password(SYSNAME,USERNAME).encode('ascii')
cmdline = [COMMAND, OPTION1, OPTION2, HOST]
cmd = subprocess.Popen(cmdline, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
cmd.stdin.write('1\n\n')
print cmd.stdin.write(str('%s\n' % password))
cmd.stdin.write('PUSH\n\n')
for line in iter(cmd.stdout.readline,""):
    print line