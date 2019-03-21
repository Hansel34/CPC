from sys import stdin, stdout
n,q = [int(x) for x in stdin.readline().split()]

bit_tree = [0]*(n+1)

def getsum(i):
    sum = 0
    i+=1
    while i > 0:
        sum+= bit_tree[i]
        i -= (i & -i)
    return sum

def update(i,v):
    i+=1
    while i<= n:
        bit_tree[i]+=v
        i += (i & -i)

for _ in range(q):
    line = stdin.readline().split()
    if line[0] == '+':
        update(int(line[1]),int(line[2]))
    else:
        stdout.write(str(getsum(int(line[1])-1))+ '\n')
