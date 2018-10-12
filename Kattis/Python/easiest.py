while (True):
	value = (input())
	if value == '0':
		break
	total = 0
	for char in value:
		total+=int(char)
	start = 11
	while(True):
		result = start*int(value)
		result = str(result)
		totaltwo = 0
		for char in result:
			totaltwo+=int(char)
		if totaltwo == total:
			print(start)
			break
		start+=1



