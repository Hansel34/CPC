lines = int(input())

for x in range(lines):
	line = input()
	if (line.startswith("simon says")):
		print(line[11:])
	else:
		print()