V = 4

INF = 9999
n,m,q,s = [int(x) for x in input().split()]

matrix = []

for x in range(n):
	matrix.append([])
	for y in range(n):
		matrix[x].append(0)


for x in range(m):
	u,v,w = [int(x) for x in input().split()]
	matrix[u][v] = w



for k in range(1,n+1):
	for i in range(1,n+1):
		for j in range(1,n+1):
			if(matrix[i][j] > matrix[i][k]+matrix[k][j]):
				matrix[i][j] = matrix[i][k] + matrix[k][j]







