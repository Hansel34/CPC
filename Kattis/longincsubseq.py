import sys

while True:
	try:
		totalNumbers = int(raw_input())
		numbers = map(int,raw_input().split())
		memory = []
		longestCurrent = []
		for i in range(100000):
			memory.append(0)
			longestCurrent.append(None)
		memory[0] = 1
		longestCurrent[0] = [0]

		for i in range(1,len(numbers)):
			maxNumber = 0
			maxIndex = 0
			for j in range(i):
				if numbers[i]>numbers[j] and memory[j]>maxNumber:
					maxNumber = memory[j]
					maxIndex = j
			memory[i] = maxNumber + 1
			if maxNumber > 0:
				longestCurrent[i] = longestCurrent[maxIndex][:]
				longestCurrent[i].append(i)
			else:
				longestCurrent[i] = [i]

		maxValue = 0
		longestCur = 0
		for i in range(len(numbers)):
			if maxValue<memory[i]:
				maxValue = memory[i]
				longestCur = i
		print(maxValue)
		for p in longestCurrent[longestCur]:
			sys.stdout.write(str(p) + " ")

	except EOFError:
		break