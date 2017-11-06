totalTime = 0
answersCorrect = 0
lst = {}

while True:
	a = input()
	if (a == '-1'):
		break
	else:
		ab = a.split()
		time = int(ab[0])
		value = ab[1]
		correct = ab[2]
		if correct == 'right':
			totalTime += time
			answersCorrect += 1
			if(lst.get(value)!=None):
				totalTime += lst[value]*20
		elif correct == 'wrong':
			if(lst.get(value)==None):
				lst[value] = 1
			else:
				lst[value] += 1

print (answersCorrect, " ", totalTime)