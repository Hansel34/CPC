from decimal import *

testCase = int(input())

for x in range(testCase):
	b,p = [float(a) for a in input().split()]
	bpm = 60*b/p
	minabpm = bpm - 1/b*bpm
	maxabpm = bpm + 1/b*bpm
	print("{:.4f} {:.4f} {:.4f}".format(minabpm,bpm,maxabpm))