

n,m,k = [int(x) for x in input().split()]

graph = {x:{} for x in range(n)}

for _ in range(m):
    one,two = [int(x) for x in input().split()]
    graph[one][two]= True
    graph[two][one]= True

visited = [False]*n

for i in range (n):
    if visited[i] == 0:
        for j in graph[i]:
            if visited[j] == False:
                visited[i] = True
                visited[j] = True
                break

print (visited.count(True))