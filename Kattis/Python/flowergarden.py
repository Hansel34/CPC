cases = int(input())

for a in range (cases):
	flower, distance = [int(x) for x in input().split()]
	currentX = 0
	currentY = 0
	counter = 0
	for b in range(flower):
		fx, fy = [int(x) for x in input().split()]
		distance -= (abs(currentX-fx)**2 + abs(currentY-fy)**2)**0.5
		currentX = fx
		currentY = fy
		if distance < 0:
			continue
		else:
			counter += 1
	exit = False
	notPrime = False
	answer = 0
	for x in range(counter,1,-1):
		notPrime = False
		for y in range(int(x**0.5)+1,1,-1):
			if x%y==0 and x!=y:
				notPrime = True
				break
		if notPrime == False:
			print(x)
			exit = True
			break
	if exit == False:
		print(0)






