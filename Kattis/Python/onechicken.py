n, m = [int(x) for x in input().split()]


if ((m-n)==1 or (n-m)==1):
	piece = " piece"
else:
	piece = " pieces"

if (m > n):
	print ("Dr. Chaz will have " + str(m-n) + piece + " of chicken left over!")
else:
	print("Dr. Chaz needs " + str(n-m) +" more"+ piece + " of chicken!")
