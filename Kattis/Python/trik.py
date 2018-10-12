line = input()

starting = 1

for char in line:
	if char == 'A':
		if starting == 1:
			starting = 2
		elif starting == 2:
			starting = 1
	if char == 'B':
		if starting == 2:
			starting = 3
		elif starting == 3:
			starting = 2
	if char == 'C':
		if starting == 1:
			starting = 3
		elif starting == 3:
			starting = 1

print(starting)
