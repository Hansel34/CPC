from collections import defaultdict

line1 = int(input())
countries = defaultdict(list)

for x in range(line1):
	line = input()
	a,b = line.split()
	b = int(b)
	countries[a].append(b)

for key in countries:
	countries[key].sort()
outputs = int(input())

for x in range(outputs):
	line = input()
	a,b = line.split()
	b = int(b)
	print (countries[a][b-1])

