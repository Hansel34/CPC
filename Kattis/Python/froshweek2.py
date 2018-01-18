input()

tasks = [int(x) for x in input().split()]
time = [int(x) for x in input().split()]

tasks.sort()
time.sort()

length = min(len(tasks),len(time))

counter = 0
counterTask = 0
counterTime = 0

while True:
	if tasks[counterTask]<=time[counterTime]:
		counter += 1
		counterTask += 1
		counterTime += 1
	elif tasks[counterTask]>time[counterTime]:
		counterTime +=1
	if counterTime == len(time) or counterTask == len(tasks):
		break


print(counter)