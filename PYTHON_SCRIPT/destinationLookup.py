import sys

# print destination ip adress
# fromat of csv file:
# "No.","Time","Source","Destination","Protocol","Length","Version","Time","Destination Port","Type","Info"
data = []
PATH = sys.argv[1]
with open(PATH, 'r') as f:
    # read the file
    lines = f.readlines()
    for line in lines:
        # split the line
        line = line.split(',')
        data.append(line)
#add adress to dic only if doesnt exist
newData = {}
for i in range(1, len(data)):
    if data[i][3] not in newData:
        newData[data[i][3]] = 1
    else:
        newData[data[i][3]] += 1

for i in newData:
    # print without first " and last "
    print(i[1:-1])


