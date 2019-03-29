from collections import defaultdict
import sys

lines = sys.stdin.readlines()
last_name = defaultdict(list)
first_name = defaultdict(int)

for name in lines:
    f_n, l_n = name.split()
    last_name[l_n].append(f_n)
    first_name[f_n]+=1

last_name_list = sorted(list(last_name))


for name in last_name_list:
    last_name[name].sort()
    for f_n in last_name[name]:
        if first_name[f_n] == 1:
            print(f_n)
        else:
            print(f_n,name)