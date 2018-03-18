cases = int(input())


for x in range (cases):
	A,B,C,D,E,F = [int(x) for x in input().split()]
	if (B+E > C+F):
		print("Sonny and Alex are safe")
	else
