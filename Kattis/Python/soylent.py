cases = int(input())

for a in range (cases):
	x = int(input())
	answer = x/400
	if x%400 != 0:
		answer +=1

	print (int(answer))