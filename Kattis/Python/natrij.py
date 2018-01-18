line1 = [int(x) for x in input().split(':')]
line2 = [int(x) for x in input().split(':')]


secondsOne = line1[2]+line1[1]*60+line1[0]*60*60
secondsTwo = line2[2]+line2[1]*60+line2[0]*60*60

if secondsTwo >= secondsOne:
	secondsOut = secondsTwo-secondsOne
else:
	secondsOut=24*60*60-secondsOne+secondsTwo

if secondsOut==0:
	print("24:00:00")
else:
	hours = int(secondsOut/(60*60))
	secondsOut = secondsOut % (60*60)
	minutes = int(secondsOut/(60))
	seconds = secondsOut % 60
	print("{:02}:{:02}:{:02}".format(hours,minutes,seconds))

