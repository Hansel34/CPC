cases = int(input())

for a in range (cases):
	people = int(input())
	totalList = []
	for x in range(people):
		pieces = [int(x) for x in input().split()]
		total = 0
		for b in range(1,len(pieces)):
			total+=pieces[b]
		totalList.append(total)
	totalList.sort()
	counter = 0
	total = 0
	for x in totalList:
		total += counter+x
		counter += x
	print(total/people)


