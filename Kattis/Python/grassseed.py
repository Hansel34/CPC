c = float(input())
lawns = int(input())
cost = 0
for line in range(lawns):
    w,l = [float(x) for x in input().split()]
    cost+=w*l*c
print(cost)