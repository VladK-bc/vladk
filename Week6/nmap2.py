#!/usr/bin/python3
#VladK nmap2

import csv
import nmap3

def read_ips(file):
    with open(file, newline='') as f:
        return [row['IP'] for row in csv.DictReader(f)]

def scan_os_and_ports(ip):
    nmap = nmap3.Nmap()
    os_results = nmap.nmap_os_detection(ip)
    os_family = 'Unknown'
    if os_results and isinstance(os_results[ip]['osmatch'], list) and os_results[ip]['osmatch'][0].get('osclass'):
        os_family = os_results[ip]['osmatch'][0]['osclass'].get('osfamily', 'Unknown')
    else:
        print(f"OS detection results for IP {ip}: {os_results}")
    open_ports = nmap.scan_top_ports(ip)
    open_ports_list = ','.join([str(port_info['portid']) for port_info in open_ports[ip]['ports']])
    return {'IP': ip, 'OpenPorts': open_ports_list, 'OSType': os_family}

def write_csv(data, file):
    with open(file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['IP', 'OpenPorts', 'OSType'])
        writer.writeheader()
        writer.writerows(data)

def main():
    input_csv = 'nmap1.csv'
    output_csv = 'nmap2.csv'

    ip_list = read_ips(input_csv)
    scanned_data = [scan_os_and_ports(ip) for ip in ip_list]

    write_csv(scanned_data, output_csv)

if __name__ == '__main__':
    main()
