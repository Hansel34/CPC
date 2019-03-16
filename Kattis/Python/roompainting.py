import bisect
n,m = [int(x) for x in input().split()]

cans = []

for _ in range(n):
    cans.append(int(input()))

cans.sort()
waste = 0

for _ in range(m):
    amount = int(input())
    waste+= cans[bisect.bisect_left(cans,amount)] - amount
    
print(waste)
