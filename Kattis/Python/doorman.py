from collections import deque

absdiff = int(input())
line = deque(input())

male = 0
female = 0


while line:
	if abs(male-female) < absdiff:
		person = line.popleft()
		if person == 'M':
			male+=1
		else:
			female+=1
	else:
		person1 = line.popleft()
		if male > female:
			if person1 == "W":
				female+=1
				continue
		else:
			if person1 == 'M':
				male+=1
				continue
		if line:
			person2 = line.popleft()
			if person1 != person2:
				line.appendleft(person1)
				line.appendleft(person2)
			else:
				break
print(male+female)
	


