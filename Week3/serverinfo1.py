#!/usr/bin/python3
#VladK serverinfo1.py

import socket
import psutil
import platform
import subprocess

def get_hostname():
    return socket.gethostname()

def get_cpu_count():
    return psutil.cpu_count()

def get_ram_gb():
    return round(psutil.virtual_memory().total / (1024.0 ** 3))

def get_os_type():
    return platform.system()

def get_os_version():
    return platform.release()

def get_disk_count():
    physical_disks = set()
    for partition in psutil.disk_partitions(all=True):
        if partition.device.startswith('/dev/sd'):
            physical_disks.add(partition.device[:8])
    return len(physical_disks)

def get_ip_mac_address():
    ip_process = subprocess.Popen(['ip', 'addr', 'show'], stdout=subprocess.PIPE)
    ip_output, _ = ip_process.communicate()

    ip_address = None
    mac_address = None

    for line in ip_output.decode().split('\n'):
        if 'inet ' in line and '127.0.0.1' not in line:
            ip_address = line.strip().split(' ')[1].split('/')[0]
        elif 'link/ether' in line:
            mac_address = line.strip().split(' ')[1]

    return (ip_address, mac_address)

if __name__ == '__main__':
    print(f"Hostname: {get_hostname()}")
    print(f"CPU (count): {get_cpu_count()}")
    print(f"RAM (GB): {get_ram_gb()}")
    print(f"OSType: {get_os_type()}")
    print(f"OSVersion: {get_os_version()}")
    print(f"Physical Disks (Count): {get_disk_count()}")
    ip_address, mac_address = get_ip_mac_address()
    if ip_address is not None:
        print(f"ip of eth0: {ip_address}")
    if mac_address is not None:
        print(f"mac of eth0: {mac_address}")
