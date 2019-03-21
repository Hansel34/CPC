from sys import stdin
w = int(input())
N = int(input())
total_area = 0
lines = stdin.readlines()
for line in lines:
    length,width = [int(x) for x in line.split()]
    total_area+=length*width
    
print(int(total_area/w))
