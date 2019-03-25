import sys
sys.setrecursionlimit(999999)

from collections import defaultdict

test_cases = int(input())

for _ in range(test_cases):
    n,m,l = [int(x) for x in input().split()]

    graph = defaultdict(list)
    visited = set()

    def dfs(i):
        if i not in visited:
            visited.add(i)
            for j in graph[i]:
                dfs(j)

    for _ in range(m):
        x, y = [int(x) for x in input().split()]
        graph[x].append(y)
    for _ in range(l):
        dfs(int(input()))

    print(len(visited))