denom = int(input())
values = [int(x) for x in input().split()]

total = 0


for value in values:
	if value == -1:
		denom -= 1
	else:
		total+=value
print(float(total/denom))