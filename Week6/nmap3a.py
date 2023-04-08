#!/usr/bin/python3
#VladK nmap3

import csv
import subprocess
import re



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
            results.append({'DNS': dns, 'IP': ip})

    return results

def write(data):
    
    with open('nmap3a.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['DNS', 'IP'])
        writer.writeheader()
        writer.writerows(data)

def main():
    
    results = dns_scan()
    write(results)

if __name__ == '__main__':

    main()
