#!/usr/bin/env python
"""Dictionary implementation for demonstrating a
   Python dictionary."""

import subprocess

def MyNetworkAddress():
    popen_obj = subprocess.Popen(("ifconfig", "en0"), stdout=subprocess.PIPE)
    open_pipe = popen_obj.stdout
    words = open_pipe.read().split()
    index = words.index("inet")
    return words[index +1]
print MyNetworkAddress()
