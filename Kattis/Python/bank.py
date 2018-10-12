N,T = [int(x) for x in input().split()]

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
