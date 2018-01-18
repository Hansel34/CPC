import math
from decimal import *

while True:
	try:
		number = int(input())
	except EOFError:
		break
	totalNumber = number*int(math.log10(number))-number+int(math.log10(math.sqrt(2*math.pi*number)))+1
	print(totalNumber)