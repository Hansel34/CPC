#square root decomposition

n,k=[int(x) for x in input().split()]

bk = int(n**.5)+2
bucket= int((n-1)/bk+1)

arr = []
for x in range(n):
	arr.append(0)
buck = []
for x in range(bucket):
	buck.append(0)


for x in range(k):
	line = input().split()
	if (line[0]=='F'):
		value = int(line[1])-1
		if arr[value] == 0:
			arr[value] = 1
			buck[int(value/bk)]+=1
		else:
			arr[value] = 0
			buck[int(value/bk)]-=1

	if (line[0]=='C'):
		total = 0
		value1 = int(line[1])-1
		value2 = int(line[2])-1
		for y in range (len(buck)):
			a = bk*y
			b = a + bk-1
			if value1<=a and b <= value2:
				total += buck[y]

			elif b < value1 or value2 < a:
				continue
			else:
				for i in range (max(value1,a),min(b,value2)+1):
					total += arr[i]
		print(total)



