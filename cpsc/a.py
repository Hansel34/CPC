cases = int(input())

keyboard = []

keyboard.append(['Q','W','E','R','T','Y','U','I','O','P'])
keyboard.append(['A','S','D','F','G','H','J','K','L'])
keyboard.append(['Z','X','C','V','B','N','M'])

for x in range (cases):
	line = input()
	start = 'E'
	total = 0
	for letter in line:
		for a,b in enumerate(keyboard):
			for c,d in enumerate(b):
				if (d == start):
					startX = a
					startY = c
				if (d == letter):
					endX = a
					endY = c
				if (d == ' '):
					startX = 0
					startY = 0
					endX = 0
					endY = 0
		start = letter
		total += 2*(abs(endY-startY)+ abs(endX-startX))
		total += 1
		if letter == ' ':
			total +=4
	print (total)