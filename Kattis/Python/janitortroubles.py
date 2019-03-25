from math import sqrt

a,b,c,d = [int(x) for x in input().split()]
s = sum([a,b,c,d])/2
print(sqrt((s-a)*(s-b)*(s-c)*(s-d)))