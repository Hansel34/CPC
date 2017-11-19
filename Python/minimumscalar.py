testcases = int(input())
case = 1

for x in range(testcases):
	input()
	list1 = [int(a) for a in input().split()]
	list2 = [int(a) for a in input().split()]

	list1.sort(reverse=True)
	list2.sort()

	total = 0

	for a in range(len(list1)):
		total += list1[a]*list2[a]

	print("Case #{}: {}".format(case,total))
	case+=1