#!/usr/bin/python3
#VladK nmaptester

import csv
import nmap3
nmap = nmap3.Nmap()

os_results = nmap.nmap_os_detection("152.157.64.4")

print (os_results)
