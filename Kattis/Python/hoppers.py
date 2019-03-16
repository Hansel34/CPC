class UnionFind:
    def __init__(self,N):
        self.count = N
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
        self.count-=1
N,M = [int(x) for x in input().split()]

hosts = UnionFind(M)

for _ in range(M):
    x,y = [int(x) for x in input().split()]
    hosts.union(x,y)
    
print(hosts.count)