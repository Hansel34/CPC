from collections import defaultdict


cards = defaultdict(int)

N,T,K = [int(x) for x in input().split()]

numbers = [int(x) for x in input().split()]

for num in numbers:
	cards[num-1] += 1
sort = []



for x in range(T):
	buy,sell = [int(x) for x in input().split()]
	if(cards[x] == 2):
		sort.append([sell+sell,-1])
	elif(cards[x] == 1):
		sort.append([sell+buy,buy])
	else:
		sort.append([buy+buy,-2])

sort.sort()


combos = 0
price = 0

for x in range(T):
	if sort[x][1] > 0 and combos == K:
		price += sort[x][0]-sort[x][1]
	elif sort[x][1] > 0 and combos < K:
		price -= (sort[x][1])
		combos +=1	

	if sort[x][1] == -1 and combos == K:
		price += sort[x][0]			
	elif sort[x][1] == -1 and combos < K:
		combos +=1		


	if sort[x][1] == -2 and combos == K:		
		continue
	elif sort[x][1] == -2 and combos < K:
		price-= sort[x][0]
		combos +=1


print(price)

