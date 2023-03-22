#!/usr/bin/python3
#Vlad K ping1

import subprocess
import sys
import pinglib
import os

filename = sys.argv[1]

with open(filename) as f:
    for line in f:
       ip_address  =line.strip()
       pinglib.pingthis(ip_address)
   