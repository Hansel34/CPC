H,W,N,M = [int(x) for x in input().split()]
image = []
kernel = []
flippedKernel = []
answer = []

for x in range(H):
	temp = [int(x) for x in input().split()]
	image.append(temp)

for x in range(N):
	temp = [int(x) for x in input().split()]
	kernel.append(temp)

for x in range (N):
	temp = [0]*M
	flippedKernel.append(temp);

for x in range (N):
	for y in range (M):
		flippedKernel[x][y]=kernel[N-x-1][M-y-1]

for x in range (H-N+1):
	temp = [0]*(W-M+1)
	answer.append(temp)


for x in range (H-N+1):
	for y in range (W-M+1):
		tempAnswer = 0;
		for a in range(N):
			for b in range(M):
				tempAnswer+= image[x+a][y+b]*flippedKernel[a][b]
		answer[x][y]=tempAnswer

for x in range(H-N+1):
	print (*answer[x], sep=" ")