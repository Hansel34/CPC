from collections import defaultdict

cities = int(input())

for _ in range(cities):
    graph = defaultdict(list)
    vertex = int(input())
    edges = int(input())
    for _ in range(edges):
        a,b = [int(x) for x in input().split()]
        graph[a].append(b)
        graph[b].append(a)
    visited = set()

    def dfs(i):
        visited.add(i)
        for j in graph[i]:
            if j not in visited:
                dfs(j)

    connected = 0
    for i in range(vertex):
        if i not in visited:
            dfs(i)
            connected+=1

    print(connected-1)