n,m = [int(x) for x in input().split()]

p = [x for x in range(n)]

def find(x):
    if p[x] == x:
        return x
    else:
        p[x] = find(p[x])
        return p[x]

def unite(x,y):
    p[find(x)]= find(y)

for _ in range(m):
    one,two = [int(x) for x in input().split()]
    unite(one-1,two-1)

connected = True
for x in range(1,n):
    if find(0) != find(x):
        print(x+1)
        connected = False

if connected == True:
    print("Connected")


