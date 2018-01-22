

def checkForWater(matrix,x,y):
	count = 0
	if matrix[x][y] == 0:
		if matrix[x-1][y]==1 :
			count = count + 1
		if matrix[x+1][y]==1 :
			count = count + 1
		if matrix[x][y-1]==1 :
			count = count + 1
		if matrix[x][y+1]==1 :
			count = count + 1
	if count == 4 or count == 0:
		return 0
	else:

		return count


n,m = [int(x) for x in input().split()]
matrix = []

emptyZeroes = [0]*(m+4)
matrix.append(emptyZeroes)
matrix.append(emptyZeroes)

visited = []
for x in range(n+4):
    visited.append([0]*(m+4))

for x in range(n):
	line = input()
	line = [int(d) for d in str(line)]
	line = [0,0] + line + [0,0]
	matrix.append(line)

matrix.append(emptyZeroes)
matrix.append(emptyZeroes)

result = 0

stack = [[1,1]]
visited[1][1] = 1
while stack:
	visiting = stack.pop()
	x = visiting[0]
	y = visiting[1]
	result = result + checkForWater(matrix,x,y)
	if(x>1):
		if(matrix[x-1][y]==0 and visited[x-1][y]==0):
			stack.append([x-1,y])
			visited[x-1][y] = 1
	if(x<n+2):
		if(matrix[x+1][y]==0 and visited[x+1][y]==0):
			stack.append([x+1,y])
			visited[x+1][y] = 1
	if(y>1):
		if(matrix[x][y-1]==0 and visited[x][y-1]==0):
			stack.append([x,y-1])
			visited[x][y-1] = 1
	if(y<m+2):
		if(matrix[x][y+1]==0 and visited[x][y+1]==0):
			stack.append([x,y+1])
			visited[x][y+1] = 1



print(result)

