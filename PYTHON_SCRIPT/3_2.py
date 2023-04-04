import os
import sys


arg = sys.argv[1]


dic_of_ip = {}
with open(arg, 'r') as f:
    lines = f.readlines()
    for line in lines:
       # add to dictionary every ip and its count if new ip add it to dictionary
        # if ip already exist in dictionary increase its count by 1
        # exemple 13.107.42.16=2, must remove the =2
        ip = line.split("=")[0]
        if ip in dic_of_ip and number[:-1] == '5':
            dic_of_ip[ip] += 1
        else:
            if number[:-1] == '5':
                dic_of_ip[ip] = 1

sorted_dic = sorted(dic_of_ip.items(), key=lambda x: x[1], reverse=True)

# print a csv of sorted dictionary
with open('output.csv', 'w') as f:
    for key, value in sorted_dic:
        f.write("%s,%s" % (key, value))
        f.write("\n")

        
