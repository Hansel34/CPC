m, n = [int(x) for x in input().split()]
matrix = []
for _ in range(m):
    matrix.append([c for c in input()])

visited = set()

def dfs(i,j):
    if i < 0 or i > m - 1 or j < 0 or j > n - 1:
        return
    if (i,j) not in visited and matrix[i][j] == '#':
        visited.add((i,j))
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                dfs(i+x,j+y)


count = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == '#' and (i,j) not in visited:
            count+=1
            dfs(i,j)
print(count)