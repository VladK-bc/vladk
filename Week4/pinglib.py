#!/usr/bin/python3
#Vlad K pinglib

import sys
import subprocess

def main():
    ip = sys.argv[1]
    result = ping(ip)
    print(result)

def ping(ip):
