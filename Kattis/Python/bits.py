cases = int(input())

for a in range (cases):
	line = input()

	max_count = 0
	for i in range(1,len(line)+1):
		max_count = max(str(bin(int(line[0:i]))).count('1'),max_count)

	print (max_count)


