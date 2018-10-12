n,m = [int(x) for x in input().split()]
boat = []

for x in range(1,m+1):
	line = input()
	if line not in boat:
		boat.append(line)
		n = n-1
	if n == 0:
		print(x)
		exit()
print("paradox avoided")