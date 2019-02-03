import math

R, C = [int(x) for x in input().split()]

inner = (R-C)*(R-C)*math.pi
total = R*R*math.pi

print(inner/total*100)

