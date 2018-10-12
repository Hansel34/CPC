import math

H,V = [int(x) for x in input().split()]

print(math.ceil(H/math.sin(math.radians(V))))