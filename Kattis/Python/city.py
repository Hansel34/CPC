cases = int(input())




for a in range (cases):
	buildings, damage = [int(x) for x in input().split()]

	build = [int(x) for x in input().split()]
	buildDmg = [int(x) for x in input().split()]

	matrix = []
	x = 2
	while x < buildings:
		

