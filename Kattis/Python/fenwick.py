n,q = [int(x) for x in input().split()]

bit_tree = [0]*(n+2)

def getsum(i):
    s = 0
    i+=1
    while i > 0:
        s+= bit_tree[i]
        i -= (i & -i)
    return s

def updatebit(i,v):
    i+=1
    while i<= n:
        bit_tree[i]+=v
        i += (i & -i)

for _ in range(q):
    line = input().split()
    if line[0] == '+':
        updatebit(int(line[1]),int(line[2]))
    else:
        print(getsum(int(line[1])))
print(bit_tree)
