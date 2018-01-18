counter = 1

while True:
	try:
		line1 = input()
		line2 = input()
	except EOFError:
		break
	a,b = [int(n) for n in line1.split()]
	c,d = [int(n) for n in line2.split()]
	det = a*d-b*c
	anew = d/det
	bnew = -b/det
	cnew = -c/det
	dnew = a/det

	print ("Case {}:".format(counter))
	print("{} {}".format(int(anew), int(bnew)))
	print("{} {}".format(int(cnew), int(dnew)))
	counter += 1
	useless = input()

