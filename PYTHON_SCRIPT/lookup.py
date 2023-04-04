# do nslookup for each ip adress

import os
import sys

# Replace the path with the actual path of the input file
PATH = sys.argv[1]

with open(PATH, 'r') as f:
    for line in f:
        # Strip leading and trailing whitespace
        line = line.strip()
        # Check if the line starts with "nslookup"
        if(not line.startswith("nslookup")):
            print(line)
        if line.startswith("nslookup"):
            # Extract the IP address from the line
            ip_address = line.split()[1]
            if ip_address.startswith("192.168"):
                continue
            # Execute nslookup with the IP address
            # print if found otherwise nothing
            os.system("nslookup " + ip_address + " > /dev/null 2>&1 && echo " + ip_address)
            
