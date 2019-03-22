from sys import stdin,stdout

class UnionFind:
    def __init__(self,N):
        self.parent = [x for x in range(N)]
        self.rank = [0]*N

    def find(self,p):
        if p == self.parent[p]:
            return p
        self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
            
    def union(self,p,q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.rank[rootQ]>self.rank[rootP]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            if self.rank[rootP] == self.rank[rootQ]:
                self.rank[rootP]+=1

N,Q = [int(x) for x in stdin.readline().split()]

union = UnionFind(N)

for _ in range(Q):
    line = stdin.readline().split()
    if line[0] == '?':
        if union.find(int(line[1])) == union.find(int(line[2])):
            stdout.write("yes"+'\n')
        else:
            stdout.write("no"+'\n')
    if line[0] == '=':
        union.union(int(line[1]),int(line[2]))