import sys
sys.setrecursionlimit(99999)

case = 1
while True:
    try:
        m, n = [int(x) for x in input().split()]
        matrix = []
        for _ in range(m):
            matrix.append([c for c in input()])

        visited = set()

        def dfs(i,j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1:
                return
            if (i,j) not in visited and matrix[i][j] == '-':
                visited.add((i,j))
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)

        count = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '-' and (i,j) not in visited:
                    count+=1
                    dfs(i,j)
        print("Case {}: {}".format(case,count))
        case+=1
    except EOFError:
        break
