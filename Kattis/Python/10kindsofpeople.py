from collections import deque

r,c = [int(x) for x in raw_input().split()]

matrix = []

for _ in range(r):
    matrix.append([int(x) for x in raw_input()])

visited = [[False for _ in range(c)] for _ in range(r)]

group = 0
group_d = {}

for i,row in enumerate(matrix):
    for j,val in enumerate(row):
        if visited[i][j] == False:
            queue = deque()
            queue.append([i,j])
            while queue:
                a,b = queue.popleft()
                if a < 0 or a >= r or b < 0 or b >= c:
                    continue
                if visited[a][b] == True:
                    continue
                if matrix[a][b] == val:
                    group_d[(a,b)] = group
                    visited[a][b] = True
                    queue.append([a,b+1])
                    queue.append([a,b-1])
                    queue.append([a+1,b])
                    queue.append([a-1,b])
            group+=1
queries = int(input())

for _ in range(queries):
    r1,c1,r2,c2 = [int(x) for x in raw_input().split()]

    if group_d[(r1-1,c1-1)] == group_d[(r2-1,c2-1)]:
        if matrix[r1-1][c1-1] == 0:
            print("binary")
        else:
            print("decimal")
    else:
        print("neither")
