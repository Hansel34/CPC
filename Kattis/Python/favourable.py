def visit(n):
	if memory.get(n) != None:
		return memory[n]
	else:
		memory[n] = visit(pages[n][0])+visit(pages[n][1])+visit(pages[n][2])
		return memory[n]



testCases = int(input())

for x in range(testCases):
	sections = int(input())
	memory = {}
	pages = {}
	for y in range(sections):
		line = input().split()
		if len(line) == 2:
			if line[1] == "favourably":
				memory[int(line[0])] = 1
			else:
				memory[int(line[0])] = 0 
		if len(line) == 4:
			pages[int(line[0])] = [int(x) for x in line[1:4]]

	print(visit(1))
	


