intructions = []
ymax = 0
ymin = 0
xmax = 0
xmin = 0
ycurrent = 0
xcurrent = 0

while True:
	try:
		line = input()
	except EOFError:
		break
	intructions.append(line)


for x in intructions:
	if x == "down":
		ycurrent-=1
	if x == "up":
		ycurrent+=1

	if ycurrent < ymin:
		ymin = ycurrent
	if ycurrent > ymax:
		ymax = ycurrent

	if x == "left":
		xcurrent-=1
	if x == "right":
		xcurrent+=1

	if xcurrent < xmin:
		xmin = xcurrent
	if xcurrent > xmax:
		xmax = xcurrent
xrng = xmax-xmin+3
yrng = ymax-ymin+3

Map = [[" " for x in range(xrng)] for y in range(yrng)]

for y in range (yrng):
	for x in range (xrng):
		if x == 0 or x == xrng-1 or y==0 or y == yrng-1:
			Map[y][x] ="#"

xs = xcurrent = xrng-xmax-2
ys = ycurrent = 0+ymax+1
for x in intructions:
	if x == "down":
		ycurrent+=1
	if x == "up":
		ycurrent-=1
	if x == "left":
		xcurrent-=1
	if x == "right":
		xcurrent+=1
	Map[ycurrent][xcurrent]="*"
Map[ys][xs]='S'
Map[ycurrent][xcurrent]="E"

for y in range (yrng):
	for x in range (xrng):
		print(Map[y][x], end="", sep="")
	print()


	







