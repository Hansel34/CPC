while True:
	actions = int(input())
	currentNumber2 = 0
	currentNumber1 = 0
	if actions == 0:
		break
	for x in range(actions):
		line = input()
		a,b = line.split()
		b = int(b)
		if a == "DROP":
			print ("DROP 2 {}".format(b))
			currentNumber2 += b
		if a == "TAKE":
			if currentNumber1 >= b:
				print("TAKE 1 {}".format(b))
				currentNumber1 -= b
			else: 
				if currentNumber1 != 0:
					print("TAKE 1 {}".format(currentNumber1))
					b -= currentNumber1
					currentNumber1 = 0
				print ("MOVE 2->1 {}".format(currentNumber2))
				currentNumber1 = currentNumber2
				currentNumber2 = 0
				print("TAKE 1 {}".format(b))
				currentNumber1 -= b
	print()
