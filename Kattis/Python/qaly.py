p = int(input())
quality = 0
for _ in range(p):
    q,t = [float(x) for x in input().split()]
    quality+= t*q
print(quality)