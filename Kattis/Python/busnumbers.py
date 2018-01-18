useless = input()
bus = input()
counter=0
prt = True

buses = [int(x) for x in bus.split()]
buses.sort()

for x in range(len(buses)-1):
	if buses[x]+1==buses[x+1]:
		counter+=1
		prt = False
	else:
		prt = True

	if counter == 0 and prt == True:
		print(buses[x], end=" ")
	if counter == 1 and prt == True:
		print(buses[x-1], " ", buses[x]," ", end = "", sep="")
		counter = 0
	if counter > 1 and prt == True:
		print(buses[x-counter], "-", buses[x]," ",end= "", sep="")
		counter = 0


if counter == 0:
	print (buses[len(buses)-1])
if counter == 1:
	print (buses[len(buses)-2],buses[len(buses)-1])
if counter >1:
	print(buses[len(buses)-1-counter], "-", buses[len(buses)-1],sep="")
	