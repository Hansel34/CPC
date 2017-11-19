line1 = input()
line2 = input()

line1new = ""
line2new = ""
l1 = len(line1)
l2 = len(line2)

if l1>l2:
	rng = l1
	for x in range(l1-l2):
		line2 = '0'+line2
else:
	rng = l2
	for x in range(l2-l1):
		line1 = '0'+line1

line1 = line1

for x in range(rng):
	if int(line1[rng-x-1]) > int(line2[rng-x-1]):
		line1new=line1[rng-x-1] + line1new
	if int(line1[rng-x-1]) < int(line2[rng-x-1]):
		line2new=line2[rng-x-1] + line2new
	if int(line1[rng-x-1]) == int(line2[rng-x-1]):
		line1new=line1[rng-x-1] + line1new
		line2new=line2[rng-x-1] + line2new

if line1new == "":
	print("YODA")
else:
	print(int(line1new))

if line2new == "":
	print("YODA")
else:
	print(int(line2new))
