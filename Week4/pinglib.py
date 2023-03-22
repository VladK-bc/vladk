#!/usr/bin/python3
#Vlad K pinglib

import subprocess
import sys
import os


def main():
    ip_address = sys.argv[1]
    pingthis(ip_address)
    

def pingthis(ip_address):
    ping_output = subprocess.run(['ping', '-c', '1', ip_address], capture_output=True)

    if ping_output.returncode == 0:
        time_ms = float(ping_output.stdout.split(b"time=")[1].split(b" ")[0])
        print(ip_address, time_ms, sep=",")
    else:
        print(ip_address, ',Not Found')
    
if __name__ == '__main__':
    main()