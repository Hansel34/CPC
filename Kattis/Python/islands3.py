r,c = [int(x) for x in input().split()]

matrix = []

for _ in range(r):
    matrix.append([c for c in input()])

def dfs(i,j):
    if i<0 or i >= r or j < 0 or j >= c:
        return
    if matrix[i][j] == 'C' or matrix[i][j] == 'L':
        matrix[i][j] = 'W'
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)

islands = 0
for i,row in enumerate(matrix):
    for j, val in enumerate(row):
        if val == 'L':
            dfs(i,j)
            islands+=1
print(islands)