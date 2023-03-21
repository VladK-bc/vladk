import socket
import psutil
import platform
import netifaces
import json
import csv
import sys

# Get hostname
hostname = socket.gethostname()

# Get CPU count
cpu_count = psutil.cpu_count(logical=False)

# Get RAM quantity
ram_bytes = psutil.virtual_memory().total
ram_gb = round(ram_bytes / (1024 ** 3), 2)

# Get OS type and version
os_type = platform.system()
os_version = platform.release()

# Get number of drives
num_drives = len(psutil.disk_partitions())

# Get IP and MAC address of eth0
interfaces = netifaces.interfaces()
for interface in interfaces:
    if interface == 'eth0':
        eth0_addrs = netifaces.ifaddresses(interface)
        ip_address = eth0_addrs[netifaces.AF_INET][0]['addr']
        mac_address = eth0_addrs[netifaces.AF_LINK][0]['addr']

# Print the results
print(f"Hostname: {hostname}")
print(f"CPU count: {cpu_count}")
print(f"RAM quantity: {ram_gb} GB")
print(f"OS type: {os_type}")
print(f"OS version: {os_version}")
print(f"Number of drives: {num_drives}")
print(f"IP address of eth0: {ip_address}")
print(f"MAC address of eth0: {mac_address}")
