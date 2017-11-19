n,w,h = [int(x) for x in input().split()]

for x in range(n):
	matchSize = int(input())
	if matchSize <= (w**2 + h**2)**0.5:
		print("DA")
	else:
		print("NE")