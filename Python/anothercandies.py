x = int(input())

for a in range(x):
	nothing = input()
	y = int (input())
	total = 0
	for b in range(y):
		temp = int(input())
		total += temp
	if (total % y == 0):
		print ("YES")
	else:
		print ("NO")