#!/usr/bin/python3
#Vlad K maillog


import sys
import re
import csv

file_name = sys.argv[1]
servers = set()
pattern = r'.*disconnect from (\S+)\[(\d+\.\d+\.\d+\.\d+)\].*'

with open(file_name, 'r') as file:
    for line in file:
        if 'disconnect' in line:
            match = re.match(pattern, line)
            if match:
                server_name = match.group(1)
                ip_address = match.group(2)
                servers.add((server_name, ip_address))

with open('servers.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Server Name', 'IP Address'])
    for server in servers:
        writer.writerow([server[0], server[1]])