#!/usr/bin/python3
#VladK nmap2

import csv
import nmap3
nmap = nmap3.Nmap()


with open('nmap1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  
    data = list(reader)

with open('nmap2.csv', 'w', newline='') as csvfile:
    fieldnames = ['IP Address', 'Open Ports', 'OS Type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in data:
        ip = row[0]
        ports = row[1]
        os_results = nmap.nmap_os_detection(ip) ##-O --osscan-guess
        ##known results, Oracle VirtualBox, iPXE, Windows

        if ip in os_results:
            highest_accuracy = 0
            os_type = ""
            for os_class in os_results[ip]['osmatch']:
                if int(os_class['accuracy']) > highest_accuracy:
                    highest_accuracy = int(os_class['accuracy'])
                    os_type = os_class['name']

            writer.writerow({'IP Address': ip, 'Open Ports': ports, 'OS Type': os_type})
        else:
            print(f"No result for OS Type {ip}")