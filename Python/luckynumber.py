n = int(input())

count = 0;
minrange = 10**n
maxrange = 10**(n+1)-1
for x in range(100,999):
	if x%3==0 and x%2==0:
		count+=1
print (count)