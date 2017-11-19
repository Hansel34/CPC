absdiff = int(input())
people = input()
male = 0
female = 0

for char in people:
	if char == 'M':
		male +=1
	else:
		female +=1
	if abs(male-female) > absdiff:
		print(male+female)
		quit()
print(male+female)

