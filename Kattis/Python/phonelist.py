trials = int(input())

for x in range(trials):
	numbers = int(input())
	number = []
	for y in range(numbers):
		number.append(input())
	number.sort()
	isNo = False 
	for x in range(1,len(number)):
		if (number[x].startswith(number[x-1])):
			print("NO")
			isNo = True
			break
	if isNo == False:
		print("YES")