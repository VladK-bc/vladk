#!/usr/bin/python3
#Vlad K Logs2



import gzip
import re
import csv

with gzip.open("dhcpdsmall.log.gz", "rt") as log_file:
    mac_addresses = {}
    for line in log_file:
        if "DHCPACK" in line:
            mac_match = re.search(r"([0-9a-f]{2}:){5}[0-9a-f]{2}", line)
            ip_match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
            if mac_match and ip_match:
                mac_address = mac_match.group(0)
                ip_address = ip_match.group(0)
                if mac_address in mac_addresses:
                    mac_addresses[mac_address]["ip_address"] = ip_address
                    mac_addresses[mac_address]["requests"] += 1
                else:
                    mac_addresses[mac_address] = {"ip_address": ip_address, "requests": 1}

with open("acklist.csv", "w", newline="") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["MAC Address", "IP Address", "Request Count"])
    for mac_address, data in mac_addresses.items():
        writer.writerow([mac_address, data["ip_address"], data["requests"]])
