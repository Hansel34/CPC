lstOfPalindromes = []


for x in range (100,1000):
	beginning = str(x)
	end = beginning[::-1]
	lstOfPalindromes.append(int(beginning+end))


number = int(input())

for x in range(number):
	palindrome = int(input())
	absdiff = 999999
	for palins in lstOfPalindromes:
		if abs(palindrome-palins) < absdiff:
			absdiff = abs(palindrome-palins)
			palin = palins
	print (palin)


