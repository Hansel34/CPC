import sys
import math
days = int(input())
money = 100
previous = sys.maxsize

for x in range(days):
	currentMoney = int(input())
	if currentMoney>previous:
		money+=min(math.floor(money/previous),100000)*(currentMoney-previous)
	previous = currentMoney

print(money)