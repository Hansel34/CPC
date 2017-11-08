line1 = [int(x) for x in input().split(':')]
line2 = [int(x) for x in input().split(':')]


s=line2[2]-line1[2]
m=line2[1]-line1[1]
h=line2[0]-line1[0]

if(line2[2]<line1[2]):
	m-=1
if(line2[1]<line1[1]):
	h-=1

if(s<0):
	s=60+s
if(m<0):
	m=60+m
if(h<0):
	h=24+h

if h==0 and m==0 and s==0:
	print("24:00:00")
else:
	print("{:02}:{:02}:{:02}".format(h,m,s))

