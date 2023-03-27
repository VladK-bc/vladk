#!/usr/bin/python3
#Vlad K logs1


import gzip


filename = "dhcpdsmall.log.gz"
unique_macs = set()
mac_count = 0

with gzip.open(filename, 'rt') as f:
    for line in f:
        if "iPhone" in line:
            columns = line.split()
            mac_address = columns[9]
            if mac_address not in unique_macs and len(mac_address) >= 12:
                
                print(mac_address)
                unique_macs.add(mac_address)
                mac_count += 1

print(f"\n{mac_count} unique MAC address count.")
