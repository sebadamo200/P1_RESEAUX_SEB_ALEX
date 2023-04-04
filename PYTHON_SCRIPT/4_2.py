

#list of ip addresses
"""
13.107.42.16
52.168.112.66
20.185.212.106
13.107.4.52
52.113.199.175
51.144.253.41
51.137.91.111
2620:1ec:42::133
"""

import os as os
import sys as sys
import csv as csv
from collections import defaultdict


#create a list of ip addresses
list_ip = ["13.107.42.16", "52.168.112.66", "20.185.212.106", "13.107.4.52", "52.113.199.175","51.144.253.41", "51.137.91.111","2620:1ec:42::133"]

def nslookup(ip):
    #check if the ip address is ipv4 or ipv6
    if ip.count(".") == 3:
        #do nslookup for ipv4
        os.system("nslookup " + ip + " > /dev/null 2>&1 && echo " + ip)
    else:
        #do nslookup for ipv6
        os.system("nslookup -type=AAAA " + ip + " > /dev/null 2>&1 && echo " + ip)


# exemple of tcp dump
"""
"No.","Time","Source","Destination","Protocol","Length","Version","Time","Destination Port","Type","Source Port","Destination Port","Info"
"17","1.845083152","192.168.0.40","13.107.42.16","TCP","74","","","","","49630","443","49630  >  443 [SYN] Seq=0 Win=64240 Len=0 MSS=1460 SACK_PERM=1 TSval=3714858691 TSecr=0 WS=128"
"18","1.856770292","13.107.42.16","192.168.0.40","TCP","66","","","","","443","49630","443  >  49630 [SYN, ACK] Seq=0 Ack=1 Win=65535 Len=0 MSS=1440 WS=256 SACK_PERM=1"
"19","1.856803764","192.168.0.40","13.107.42.16","TCP","54","","","","","49630","443","49630  >  443 [ACK] Seq=1 Ack=1 Win=64256 Len=0"
"22","1.920547357","192.168.0.40","13.107.42.16","TLSv1.2","311","TLS 1.0","","","","49630","443","Client Hello"
"23","1.933594620","13.107.42.16","192.168.0.40","TCP","60","","","","","443","49630","443  >  49630 [ACK] Seq=1 Ack=258 Win=4194304 Len=0"
"""
# want ti know how many streams are there if i have the ip address of the destination


# destination ip address
"""
13.107.42.16
52.168.112.66
20.185.212.106
13.107.4.52
52.113.199.175
51.144.253.41
51.137.91.111
2620:1ec:42::133
"""
# ip = list of ip addresses
# file = csv file
import csv
import sys

def count_packets(ip, file):
    num_sent = 0
    num_received = 0
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Destination'] == ip and row['Protocol'] == 'TCP':
                num_sent += 1
            elif row['Source'] == ip and row['Protocol'] == 'TCP':
                    num_received += 1
    return num_sent, num_received

def count_streams(ip, file):
    streams = set()
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Destination'] == ip and row['Protocol'] == 'TCP':
                streams.add((row['Source'], row['Source Port'], row['Destination Port']))
    return len(streams)

ip_list = ['13.107.42.16', '52.168.112.66', '20.185.212.106', '13.107.4.52', '52.113.199.175', '51.144.253.41', '51.137.91.111', '2620:1ec:42::133']
file = sys.argv[1]
for ip in ip_list:
    num_streams = count_streams(ip, file)
    num_sent, num_received = count_packets(ip, file)
    print(f'For destination IP {ip}:')
    print(f'- There are {num_streams} TCP streams.')
    print(f'- {num_sent} packets were sent to the destination.')
    print(f'- {num_received} packets were received by the destination.')
