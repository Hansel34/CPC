from decimal import *

line1 = input()
value = int(line1)

one = len(line1)
level = 0
total = 0

for char in reversed(line1):
	if int(char) == 1 or int(char)==3:
		total+= 2**level
	if int(char) == 2 or int(char)==3:
		total+= (2**one)*(2**(level))
	level += 1
y = int(Decimal(total)/ Decimal((2**one)))
x = total% (2**one)
print("{} {} {}".format(one,x,y))