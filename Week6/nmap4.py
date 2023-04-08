#!/usr/bin/python3
#VladK nmap2

import csv
import subprocess
import re
import requests

#modified from nmap3a, revert if necessary for test
def dns_scan():
    command = "nmap -sn -Pn --script dns-brute nsd.org"
    output = subprocess.check_output(command, shell=True, text=True)
    ipv4_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    dns_pattern = re.compile(r'[\w.-]+\.nsd\.org')
    results = []
    for line in output.splitlines():
        dns_match = dns_pattern.search(line)
        ipv4_match = ipv4_pattern.search(line)
        if dns_match and ipv4_match:
            dns = dns_match.group()
            ip = ipv4_match.group()
            #website checkbox used
            api_url = f"http://ip-api.com/json/{ip}?fields=country,regionName,city,zip,isp"
            response = requests.get(api_url).json()
            results.append({'DNS': dns, 'IP': ip, 'Country': response['country'], 'RegionName': response['regionName'], 'City': response['city'], 'Zipcode': response['zip'], 'ISP': response['isp']})
    return results


def write(data):
    with open('nmap4.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['DNS', 'IP', 'Country', 'RegionName', 'City', 'Zipcode', 'ISP'])
        writer.writeheader()
        writer.writerows(data)


def main():
    results = dns_scan()
    write(results)


if __name__ == '__main__':
    main()
