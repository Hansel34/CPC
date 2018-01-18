import sys

mappedValues = {}

for line in sys.stdin:
	ab = (line.split())
	a = (ab[0])
	if (a == 'define'):
		b = int(ab[1])
		c = ab[2]
		mappedValues[c] = b

	else:
		b = ab[1]
		c = ab[2]	
		d = ab[3]
		if (mappedValues.get(b) == None or mappedValues.get(d) == None):
			print("undefined")
		elif (c== '<'):
			if(mappedValues.get(b)<mappedValues.get(d)):
				print("true")
			else:
				print("false")
		elif (c== '='):
			if(mappedValues.get(b)==mappedValues.get(d)):
				print("true")
			else:
				print("false")
		elif (c== '>'):
			if(mappedValues.get(b)>mappedValues.get(d)):
				print("true")
			else:
				print("false")


