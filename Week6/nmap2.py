#!/usr/bin/python3
#VladK nmap2

import csv
import nmap

def read_ips(file):
    with open(file, newline='') as f:
        return [row['IP'] for row in csv.DictReader(f)]

def scan_os(ip):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=ip, arguments='-O')
    open_ports = [str(port) for port in scanner[ip]['tcp'].keys() if scanner[ip]['tcp'][port]['state'] == 'open']
    os_family = scanner[ip].get('osclass', {}).get('osfamily', 'Unknown')
    return {'IP': ip, 'OpenPorts': ','.join(open_ports), 'OSType': os_family}

def write_csv(data, file):
    with open(file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['IP', 'OpenPorts', 'OSType'])
        writer.writeheader()
        writer.writerows(data)

def main():
    input_csv = 'nmap1.csv'
    output_csv = 'nmap2.csv'

    ip_list = read_ips(input_csv)
    scanned_data = [scan_os(ip) for ip in ip_list]

    write_csv(scanned_data, output_csv)

if __name__ == '__main__':
    main()
