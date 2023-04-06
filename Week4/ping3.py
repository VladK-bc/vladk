#!/usr/bin/python3
#VladK ping3


import sys
import subprocess
import csv
import socket
import re

def ping_addresses(addresses, output_file=None):
    results = []
#checks ip addresses and throws error code
    for address in addresses:
        try:
            response = subprocess.check_output(['ping', '-c', '1', address], stderr=subprocess.DEVNULL)
            response = response.decode('utf-8')
            match = re.search(r'time=(\d+(?:\.\d+)?) ms', response)
            if match:
                time_to_ping = match.group(1)
                result = f"{address}, {time_to_ping}"
            else:
                result = f"{address}, Not found"
        except subprocess.CalledProcessError:
            result = f"{address}, Not found"
        
        results.append(result)
#prints output
    print("IP,TimeToPing(ms)")
    for result in results:
        print(result)

    if output_file:
        with open(output_file, 'w', newline='') as csvfile:
            csvfile.write("IP,TimeToPing(ms)\n")
            for result in results:
                csvfile.write(result + "\n")
#calls main
def main():
    input_arg = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    addresses = []
#appends csv file
    try:
        socket.inet_aton(input_arg)
        addresses.append(input_arg)
    except socket.error:
        with open(input_arg, 'r') as file:
            for line in file.readlines():
                line = line.strip()
                addresses.append(line)

    ping_addresses(addresses, output_file)

if __name__ == '__main__':
    main()
