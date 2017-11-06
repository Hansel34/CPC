line1 = input()
output = []
for char in line1:
	if char != '<':
		output.append(char)
	else:
		output.pop()
for char in output:
	print(char, end='')
