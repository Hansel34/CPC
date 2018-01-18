lst = []
for x in range(10):
	value = int(input())
	if value%42 not in lst:
		lst.append(value%42)
print(len(lst))
