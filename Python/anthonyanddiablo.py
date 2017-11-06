import math

ab = input()
ab= (ab.split())
a = float(ab[0])
b = float(ab[1])

if (b**2/(4*math.pi)>a):
	print ("Diablo is happy!")
else:
	print ("Need more materials!")


