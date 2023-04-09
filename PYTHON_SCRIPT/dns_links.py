import sys
import os
import csv

path = sys.argv[1]

lst = []
with open(path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        if line['Protocol'] == 'DNS' and line['Info'].startswith('Standard query 0x'):
            line = line['Info'].split(' ')
            if line[-2] not in lst:
                lst.append(line[-2])

for i in lst:
    print(i)

""" RESPONSE 
open-ai-connect.skype.com
a.config.skype.com
pipe.skype.com
api.aps.skype.com

browser.pipe.aria.microsoft.com

onedscolprdwus14.westus.cloudapp.azure.com
onedscolprdeus08.eastus.cloudapp.azure.com
onedscolprdaus00.australiasoutheast.cloudapp.azure.com
onedscolprdwus13.westus.cloudapp.azure.com, 

azeus1-client-s.gateway.messenger.live.com 

ip.azeus1-client-s.msnmessenger.msn.com.akadns.net   

weu1-api-skype.cloudapp.net 
b-aps-euwe-01-skype.cloudapp.net
optionsservice-prod-westeurope-b.cloudapp.net

www.msftconnecttest.com

4-c-0003.c-msedge.net 


"""
