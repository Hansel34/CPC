Case = 1;

while True:
	try:
		line1 = input()
	except EOFError:
		break

	Z = 0
	IN = True
	Zx = 0
	Zy = 0
	Zxnew = 0
	Zynew = 0

	inputs = line1.split()
	x = float(inputs[0])
	y = float(inputs[1])
	r = int(inputs[2])

	for a in range(r):
		Zxnew = (Zx**2)-(Zy**2)+x
		Zynew = 2*Zx*Zy+y
		Zx = Zxnew
		Zy = Zynew
		if (Zxnew**2+Zynew**2)**0.5>2:
			IN = False
			break
	if IN == True:
		print ("Case {}: IN".format(Case))
	if IN == False:
		print ("Case {}: OUT".format(Case))
	Case += 1


	