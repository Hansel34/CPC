

testcase = int(input())

for x in range(testcase):
	garbage = input()
	numValues = int(input())
	summationValues = {}
	summationValues[0]=1
	totalValue = 0
	count = 0

	totalValues = [int(a) for a in input().split()]


	for a in totalValues:
		totalValue += a;
		summationValues[totalValue] = summationValues.get(totalValue,0) + 1;
		if totalValue-47 in summationValues:
			count += summationValues[totalValue-47]

	print(count)






