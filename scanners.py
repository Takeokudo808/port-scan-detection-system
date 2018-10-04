import os
import re
filePath = "ssh.log.txt"
line_count = 0
merge_from_ip = []
merge_against_ip= []                             
from_ip = []
against_ip = []
open_log = open(filePath, 'r')
for line in open_log:
    if 'Nmap' in line:
        line_count += 1
        line_split = line.split()
        merge_from_ip.append(line_split[2])
        from_ip = list(set(merge_from_ip))
        merge_against_ip.append(line_split[4])
        against_ip = list(set(merge_against_ip))
print('There are a total ' + str(line_count) + ' Nmap scanned events.\n')
print('Here is a list of scanned ip addresses originated from:')
for ip_addresses in from_ip:
    print(ip_addresses)
print('\r\nHere is a list of scanned ip addresses performed against:')
for performed_ip in against_ip:
    print(performed_ip)
scanned_log = open('scanners_found.txt', 'w+')
scanned_log.write('There are a total ' + str(line_count) + ' Nmap scanned events.\r\n')
scanned_log.write('Here is a list of scanned ip addresses originated from:\n')
for originate_ip in from_ip:
    scanned_log.write(str(originate_ip) + '\n')
scanned_log.write('\rHere is a list of scanned ip addresses performed against:\n')
for performed_ip in against_ip:
    scanned_log.write(str(performed_ip) + '\n')
scanned_log.close()
open_log.close()