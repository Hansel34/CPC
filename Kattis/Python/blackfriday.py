input()

totalValues = [int(x) for x in input().split()]
sortedValues = sorted(totalValues, reverse=True)
counter = 0
for x in sortedValues:
	for y in totalValues:
		if x == y:
			counter += 1
	if counter == 1:
		print(totalValues.index(x)+1)
		quit()
	counter = 0

print("none")
