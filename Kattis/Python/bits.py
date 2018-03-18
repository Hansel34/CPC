cases = int(input())

for a in range (cases):
	line = input()
	outputInt = []
	outputBin = []
	for x in range(len(line)):
		outputInt.append(line[0:x+1])
	answer = 0
	output = 0
	for x in outputInt:
		for char in str(bin(int(x))):
			if char == '1':
				answer += 1
		if answer > output:
			output = answer
		answer = 0
	print(output)


