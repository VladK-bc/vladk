#!/usr/bin/python3
#VladK nmap1


import nmap
import csv

#passes arguements to nmap, default is 1k ports. Script takes awhile to run
def scan(target):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-sS')
    return nm, nm.all_hosts()

def parse(nm, hosts):
    res = []
    for h in hosts:
        #dont touch this
        open_ports = [str(p) for p in nm[h]['tcp'].keys() if nm[h]['tcp'][p]['state'] == 'open']
        if open_ports:
            res.append({'IP': h, 'Open_Ports': ','.join(open_ports)})
    return res

#csv writer
def save(res, file):
    with open(file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['IP', 'Open_Ports'])
        writer.writeheader()
        writer.writerows(res)

def main():
    ranges = ['152.157.64.0/24', '152.157.65.0/24']
    all_res = []

    for r in ranges:
        nm, hosts = scan(r)
        res = parse(nm, hosts)
        all_res.extend(res)

        for r in res:
            print(f"{r['IP']}: {r['Open_Ports']}")
#do not confuse with main script name
    save(all_res, 'nmap1.csv')

if __name__ == '__main__':
    main()
