import sys
# Calculate the mean RTT for each flow

"""Format query in CSV file: 
    7;0.120743;2a02:2788:7d4:2bf:f53d:f6f3:5895:b823;2a02:2788:fff0:7::3;DNS;120;Standard query 0x4dae A api-flightproxy-skype.trafficmanager.net
    Format response in CSV file:
    12;0.138143;2a02:2788:fff0:7::3;2a02:2788:7d4:2bf:f53d:f6f3:5895:b823;DNS;501;Standard query response 0x4dae A api-flightproxy-skype.trafficmanager.net CNAME a-flightproxy-euno-01-skype.cloudapp.net A 13.70.198.241 NS ns1-201.azure-dns.com NS ns2-201.azure-dns.net NS ns4-201.azure-dns.info NS ns3-201.azure-dns.org AAAA 2603:1061:0:700::c9 AAAA 2620:1ec:8ec:700::c9 AAAA 2a01:111:4000:700::c9 AAAA 2620:1ec:bda:700::c9 A 40.90.4.201 A 64.4.48.201 A 13.107.24.201 A 208.84.5.201
"""
data = []
PATH = sys.argv[1]
with open(PATH, 'r') as f:
    # read the file
    lines = f.readlines()
    for line in lines:
        # split the line
        line = line.split(',')
        data.append(line)
newData = []
for i in range(1, len(data)):
    newData.append((data[i][1], data[i][-1].split(" ")[:4]))
newData = tuple(newData)

# key is like 0x4dae and values would be list of times because query and response
dictA = {}
for i in range(len(newData)):
    if newData[i][1][2] == "response":
        key = newData[i][1][3]
        if key in dictA:
            dictA[key].append(float(newData[i][0][1:-2]))
        else:
            dictA[key] = [float(newData[i][0][1:-2])]
    else:
        key = newData[i][1][2]
        if key in dictA:
            dictA[key].append(float(newData[i][0][1:-2]))
        else:
            dictA[key] = [float(newData[i][0][1:-2])]

# CALCULATE MEAN RTT from dictA
diffTot = 0
number = 0
for i in dictA:
    diffTot += abs(dictA[i][0] - dictA[i][1])
    number += 1
print('Mean RTT DNS = ', diffTot/number)
