name = input()
if (len(name) == 1):
	print(name)
	exit()

for x in range(len(name)-1):
	if name[x]!=name[x+1]:
		print(name[x], end='')
print(name[x+1])