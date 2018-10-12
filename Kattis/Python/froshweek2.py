n,m = [int(x) for x in input().split()]

tasks = [int(x) for x in input().split()]
time = [int(x) for x in input().split()]

tasks.sort()
time.sort()

counter = 0
counterTask = 0
counterTime = 0

while True:
	if tasks[counterTask]<=time[counterTime]:
		counterTask += 1
		counterTime += 1
	elif tasks[counterTask]>time[counterTime]:
		counterTime +=1
	if counterTime == n or counterTask == m:
		break

print(counterTask)
