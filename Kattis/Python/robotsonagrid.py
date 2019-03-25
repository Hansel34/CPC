import sys

n = int(raw_input())
matrix = []
for _ in range(n):
    matrix.append([c for c in sys.stdin.readline()])

visited = [[False for _ in range(n)] for _ in range(n)]
def dfs():
    stack = [[0,0]]
    while(stack):
        i,j = stack.pop()
        if visited[i][j] == False:
            if matrix[i][j] != '#':
                visited[i][j] = True
                if i > 0:
                    stack.append([i-1,j])
                if i < n -1:
                    stack.append([i+1,j])
                if j > 0:
                    stack.append([i,j-1])
                if j < n - 1:
                    stack.append([i,j+1])
    if visited[n-1][n-1]:
        return "THE GAME IS A LIE"
    else:
        return "INCONCEIVABLE"
connected = dfs()

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            if matrix[i][j] == '.':
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
        elif i == 0:
            if matrix[i][j] ==  '.':
                matrix[i][j] = matrix[i][j-1]
            else:
                matrix[i][j] = 0
        elif j == 0:
            if matrix[i][j] ==  '.':
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = 0
        else:
            if matrix[i][j] ==  '.':
                matrix[i][j] = matrix[i-1][j]+matrix[i][j-1] 
            else:
                matrix[i][j] = 0

if matrix[n-1][n-1]:
    print(matrix[n-1][n-1] % (2**31-1))
else:
    print(connected)
