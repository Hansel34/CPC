from sys import stdin

lines = stdin.readlines()

for line in lines:
    line = line.lower()
    if "problem" in line:
        print("yes")
    else:
        print("no")