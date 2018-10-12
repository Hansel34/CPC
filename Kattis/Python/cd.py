from collections import defaultdict

while True:

	N,M = map(int,raw_input().split())
	if (N==0 and M==0):
		break
	CDs = defaultdict(int)

	for x in range (N):
		CDs[int(raw_input())]+=1

	for x in range (M):
		CDs[int(raw_input())]+=1
	count = 0
	for x in CDs:
		if CDs[x]>1:
			count+=1
	print(count)

	