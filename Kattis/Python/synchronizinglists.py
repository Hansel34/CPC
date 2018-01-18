
while True:
	firstList = {}
	first = []
	second = []
	a = int(input())
	if (a == 0):
		break

	for x in range (a):
		b = int(input())
		firstList[b] = x
		first.append(b)

	for x in range (a):
		b = int(input())
		second.append(b)

	first.sort()
	second.sort()
	f = []
	for i in range(a):
		f.append(0)

	for x in range (a):
		f[firstList[first[x]]] = second[x]


	for x in range (a):
		print (f[x])

	print()
