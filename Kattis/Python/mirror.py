cases = int(input())

for a in range(cases):
	print("Test " + str(a+1))
	n,m = [int(x) for x in input().split()]
	output = []
	inp = []
	for x in range(n):
		line = input()
		inp.append([])
		for y in line:
			inp[x].append(y)
	for x in range(n):
		output.append([])
		for y in range(m):
			output[x].append(inp[n-x-1][m-y-1])
	for x in output:
		for y in x:
			print(y,end="")
		print()
