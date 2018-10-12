N,T = [int(x) for x in input().split()]

<<<<<<< HEAD
moneyAndTime = []
money = [0 for x in range(T)]

for _ in range(N):
	moneyAndTime.append([int(x) for x in input().split()])
	
moneyAndTime.sort(key=lambda x:x[0], reverse=True)

for x,y in moneyAndTime:
	for i in reversed(range(y+1)):	
		if money[i]==0:
			money[i] += x
			break

print (sum(money))
=======
timeList = []
richList = []
moneyList = []


for x in range(T):
	moneyList.append(0)

for x in range(N):
	money,time = [int(a) for a in input().split()]
	richList.append(money)
	timeList.append(time)

timeListsorted =[x for y,x in sorted(zip(richList,timeList), reverse = True)]
richList.sort(reverse=True)

for x in range(len(richList)):
	for a in reversed(range(timeListsorted[x]+1)):
		if moneyList[a] == 0:
			moneyList[a]=richList[x]
			break

print(sum(moneyList))

>>>>>>> 48ef830bab767b4bb0486497b8e1fbe0c09cc67e
