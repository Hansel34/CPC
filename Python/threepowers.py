while True:
	line = int(input())
	if line == 0:
		break
	binaryvalue=bin(line-1)
	binaryvalue = binaryvalue[2:]
	output="{ "
	count = 0
	if binaryvalue == '0':
		print("{ }")
		continue
	for x in reversed(binaryvalue):
		if x == '1':
			output= output+str(3**count)+", "
		count += 1
	output = output[:-2]+ " }"
	print(output)

