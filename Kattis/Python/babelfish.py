import sys

lines = sys.stdin.readlines()
dic = True
d = {}
for line in lines:
    line = line.rstrip()
    if line == "":
        dic = False
        continue
    if dic:
        line = line.split()
        d[line[1]] = line[0]
    else:
        if line in d:
            print(d[line])
        else:
            print("eh") 
