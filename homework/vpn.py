#Daniel Gutierrez - 09.27.2017
import keyring
import subprocess

# setup these variables
#VPNGROUP = ''  # The VPN group you are trying to connect to (numerical)
#USERNAME = print(GetUserName())  # This is the username for the vpn connection
SYSNAME = 'AnyConnect'  # This is the name of the entry in Keychain that stores your credentials
COMMAND = '/opt/cisco/anyconnect/bin/vpn'
OPTION1 = '-s'
OPTION2 = 'connect'
HOST = 'vpn.coursehero.com' #The hostname or IP of the VPN device you are trying to connect to

def GetUserName():
    while True:
        said = raw_input('Enter your username : ')
        try:
            said = str(said)
        except ValueError:
            print said, "this not a username try again"
            return
        break

def ReturnUserName():
    username = GetUserName()


# Set value for subprocess stdin to read password
password = keyring.get_password(SYSNAME,GetUserName()).encode('ascii')

#subproces for vpn command with stdin stdout pipes
cmdline = [COMMAND, OPTION1, OPTION2, HOST]
cmd = subprocess.Popen(cmdline, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
cmd.stdin.write('1\n\n')
print cmd.stdin.write(str('%s\n' % password))
cmd.stdin.write('PUSH\n\n')
#send output to stdout to stdin
for line in iter(cmd.stdout.readline,""):
    print line