testcases = int(input())
count = 0
for x in range(testcases):
	line = input()
	prev = None
	for char in line:
		if char == 'D' and prev == "C":
			count+=1
			break
		else:
			prev=char

print(testcases-count)

