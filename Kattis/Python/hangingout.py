n,m = [int(x) for x in input().split()]
notAllowed = 0
currentSum = 0

for _ in range(m):
	direc, val = input().split()
	val = int(val)
	if (direc == "enter"):
		if currentSum+ val > n:
			notAllowed+=1
		else:
			currentSum+=val
	else:
		currentSum-=val
print(notAllowed)