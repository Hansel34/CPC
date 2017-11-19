N,T = [int(x) for x in input().split()]

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

