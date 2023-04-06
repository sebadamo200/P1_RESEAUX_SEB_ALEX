import os
import sys
import csv

def list_of_protocol(arg):
    protocol_list = []
    with open(arg, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Protocol'] not in protocol_list:
                protocol_list.append(row['Protocol'])
    return protocol_list
        
def count_num_of_protocol(protocol, file):
    num = 0
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Protocol'] == protocol:
                num += 1
    return num

file = sys.argv[1]
protocol_list = ['UDP', 'DNS', 'TCP', 'TLSv1.2', 'STUN', 'RTCP', 'ARP', 'MDNS', 'ICMPv6', 'STP', 'SSDP', 'HTTP', 'XID']

for_excel = []
for protocol in protocol_list:
    num = count_num_of_protocol(protocol, file)
    for_excel.append(num)
    ## add to output file like csv

print(for_excel)

# this gives unique protocol list from the csv file
""""
protocol_list = list_of_protocol(file)
print(protocol_list)
"""

