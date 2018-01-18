
dct = {}
dct2 = {}
while True:
	unknown = False
	try:
		line = input()
	except EOFError:
		break
	splittedLine = line.split()
	if splittedLine[0] == "def":
		if dct.get(splittedLine[1])!=None:
			del dct2[dct[splittedLine[1]]]
			del dct[splittedLine[1]]
		dct[splittedLine[1]]=int(splittedLine[2])
		dct2[int(splittedLine[2])]=splittedLine[1]
		
	if splittedLine[0] == "calc":
		total = 0
		for x in range (int((len(splittedLine)-3)/2)+1):
			if(dct.get(splittedLine[x*2+1])==None):
				print(line[5:],"unknown")
				unknown = True
				break
		if dct.get(splittedLine[1]) != None:
			total += dct[splittedLine[1]]
		for x in range(int((len(splittedLine)-3)/2)):
			if(dct.get(splittedLine[x*2+3])!=None):
				if(splittedLine[x*2+2]=='+'):
					total += dct[splittedLine[x*2+3]]
				else:
					total -= dct[splittedLine[x*2+3]]

		if unknown == False:
			if dct2.get(total) == None:
				print(line[5:],"unknown")
			else:
				print(line[5:],dct2[total])

	if splittedLine[0] == "clear":
		dct.clear()
		dct2.clear()

