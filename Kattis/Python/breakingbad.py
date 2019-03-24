from collections import defaultdict

i = int(input())
items = []

for _ in range(i):
    items.append(input())

edges = int(input())
graph = defaultdict(list)

for e in range(edges):
    a,b = input().split()
    graph[a].append(b)
    graph[b].append(a)

visited = set()
group0 = set()
group1 = set()

stack = []
for item in items:
    if item not in visited:
        stack.append([item,0])
        visited.add(item)
    while stack:
        c = stack.pop()
        def add_opposite(group,num):
            group.add(c[0])
            for e in graph[c[0]]:
                if e in group:
                    print("impossible")
                    exit()
                if e not in visited:
                    stack.append([e,num])
                    visited.add(e)
        if c[1] == 0:
            add_opposite(group0,1)
    
        if c[1] == 1:
            add_opposite(group1,0)
print(" ".join(group0))
print(" ".join(group1))
