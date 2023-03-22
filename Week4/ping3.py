#!/usr/bin/python3
#VladK ping3

import subprocess
import sys
import pinglib
import os
import csv
import io
from contextlib import redirect_stdout

if len(sys.argv) < 2:
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
        

if len(sys.argv) > 2:
      csv_file = sys.argv[2]
      arg = sys.argv[1]
      if os.path.isfile(arg):
            filename = sys.argv[1]

            with open(filename) as f:
                for line in f:
                    ip_address  =line.strip()
                    result = pinglib.pingthis(ip_address)
                    with open(csv_file, 'w', newline='') as csvfile:
                         writer = csv.writer(csvfile)
                         writer.writerow(['Result'])
                         writer.writerow([result])
                         
      else:
             ip_address = sys.argv[1]
             pinglib.pingthis(ip_address)
             result = pinglib.pingthis(ip_address)
             with open(csv_file, 'w', newline='') as csvfile:
                         writer = csv.writer(csvfile)
                         writer.writerow(['Result'])
                         writer.writerow([result])
                       