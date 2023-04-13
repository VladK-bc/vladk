#!/usr/bin/python3
#Vlad K Logs3



import sys
import re
import gzip
import requests
import csv
import time

def api(mac_address):
    url = f"https://api.macvendors.com/{mac_address}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        vendor_info = response.text
        return vendor_info
    except requests.exceptions.HTTPError as e:
        return None

def matchipmacaddresses(file_path, ip_addresses):
    mac_pattern = re.compile(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})")
    ipmac = {}
    
    with gzip.open(file_path, "rt") as file:
        for line in file:
            for ip in ip_addresses:
                if ip in line:
                    macmatch = re.search(mac_pattern, line)
                    if macmatch:
                        ipmac[ip] = macmatch.group(0)

    return ipmac

def main():
    if len(sys.argv) < 2:
        print("Use command ./Logs3.py input.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    dhcp_log_file = "dhcpdsmall.log.gz"
    output_file = "output.csv"

    with open(input_file, "r") as file:
        ip_addresses = [line.strip() for line in file]

    ip_mac_map = matchipmacaddresses(dhcp_log_file, ip_addresses)

    with open(output_file, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["IP", "MAC Address", "Vendor"])

        for ip, mac_address in ip_mac_map.items():
            time.sleep(0.6)
            vendor_info = api(mac_address)
            if vendor_info:
                csvwriter.writerow([ip, mac_address, vendor_info])
            else:
                pass

if __name__ == "__main__":
    main()
