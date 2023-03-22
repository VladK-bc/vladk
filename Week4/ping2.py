#!/usr/bin/python3
#VladK ping2

import subprocess
import sys
import pinglib
import os

arg = sys.argv[1]
if os.path.isfile(arg):
            filename = sys.argv[1]

            with open(filename) as f:
                for line in f:
                    ip_address  =line.strip()
                    pinglib.pingthis(ip_address)
else:
        ip_address = sys.argv[1]
        pinglib.pingthis(ip_address)