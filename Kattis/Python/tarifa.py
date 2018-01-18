x = int(input())
months = int(input())

total = (months+1)*x

for x in range(months):
	total = total - int(input())
print(total)