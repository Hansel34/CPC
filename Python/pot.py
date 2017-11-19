testCase = int(input())
total = 0
for x in range(testCase):
	value = input()
	number = value[:-1]
	power = value[len(value)-1:]
	total += int(number)**int(power)
print(total)
