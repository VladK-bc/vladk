#!/usr/bin/python3
#VladK database3.py

import pymysql
import week7serverinfo

print(f"Hostname: {week7serverinfo.get_hostname()}")
mac_address, ip_address = week7serverinfo.get_ip_mac_address()
if mac_address is not None:
    print(f"MAC of eth0: {mac_address}")
if ip_address is not None:
    print(f"IP of eth0: {ip_address}")
print(f"CPU (count): {week7serverinfo.get_cpu_count()}")
print(f"Physical Disks (Count): {week7serverinfo.get_disk_count()}")
print(f"RAM (GB): {week7serverinfo.get_ram_gb()}")
print(f"OSType: {week7serverinfo.get_os_type()}")
print(f"OSVersion: {week7serverinfo.get_os_version()}")

