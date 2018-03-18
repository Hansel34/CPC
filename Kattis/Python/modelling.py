cases = int(input())

for a in range (cases):
	line = input()
	values = {}
	instructions = []
	x = 0
	count = 0
	while x < (len(line)):
		if line[x] == '[':
			instructions.append([])
			while line[x] != ']':
				instructions[count].append(line[x])
				x+=1 
			x+=1
			count += 1
	print(instructions)



		#else if line[x] == '(':

	#	else if line[x] == '<':
