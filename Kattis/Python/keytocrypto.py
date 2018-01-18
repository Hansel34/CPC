string1 = input()
string2 = input()
string = ''

Z= ord('Z')
A= ord('A')
for x in range(len(string1)):
	greaterThanA = ord(string1[x])-(ord(string2[x])-A)
	if greaterThanA < A:
		greaterThanA=greaterThanA+26
	string2+=chr(greaterThanA)
	string+=chr(greaterThanA)




print(string)


