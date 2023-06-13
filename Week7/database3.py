#!/usr/bin/python3
#VladK database3.py


import pymysql
import week7serverinfo

## syntax is localhost username, password, database name
db = pymysql.connect(host= 'localhost',
                     user= 'cmdb',
                     password= 'cmdb',
                     database= 'cmdb'
                     )


cursor = db.cursor()

name = week7serverinfo.get_hostname()
macaddress = week7serverinfo.get_ip_mac_address()[1]
ip = week7serverinfo.get_ip_mac_address()[0]
cpucount = week7serverinfo.get_cpu_count()
disks = week7serverinfo.get_disk_count()
ram = week7serverinfo.get_ram_gb()
ostype = week7serverinfo.get_os_type()
osversion = week7serverinfo.get_os_version()

sql = """INSERT INTO device 
        (name, macaddress, ip, cpucount, disks, ram, ostype, osversion) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

values = (name, macaddress, ip, cpucount, disks, ram, ostype, osversion)

try:
    cursor.execute(sql, values)
    db.commit()
    print("Insert Success")
except Exception as e:
    db.rollback()
    print("Data insert failed", e)

db.close()
