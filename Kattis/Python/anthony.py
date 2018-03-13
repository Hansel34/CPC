import operator as op
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, xrange(n, n-r, -1), 1)
    denom = reduce(op.mul, xrange(1, r+1), 1)
    return numer//denom


n,m = [int(x) for x in input().split()]
totalWinning = float(0)
probabilityWinning = 0
probability = []
for x in range(n+m-1):
	winningPercent = float(input())
	if (winningPercent == 1):
		n-=1
	elif (winningPercent == 0):
		m-=1
	else:
		probability.append(winningPercent)
	if n == 0:
		print (str.format('{0:.6f}', 0))
		exit()

	if m == 0:
		print (str.format('{0:.6f}', 1))
		exit()

averageWin = float(0)
for value in probability:
	averageWin+=value
averageWin = averageWin/(n+m-1)

for x in range(n,n+m)
winningChance = 

print(str.format('{0:0.6f}',winningChance))


