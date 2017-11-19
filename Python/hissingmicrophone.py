line = input()
prev = None
hiss = False

for char in line:
	if char == 's' and prev == 's':
		hiss = True
	prev = char

if hiss == True:
	print("hiss")
else:
	print("no hiss")