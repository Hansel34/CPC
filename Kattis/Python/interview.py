A,B,T,ta,tb = [int(x) for x in input().split()]

interviews = int(input())
companies = []

for x in range(interviews):
	ai, bi = [int(x) for x in input().split()]
	companies.append([ai,bi])

companies.sort()

for count,value in enumerate(companies):
	for y in range(count+1)
