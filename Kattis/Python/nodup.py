from collections import defaultdict

line = input().split()
words = defaultdict(int)

for word in line:
	words[word]+=1

for key in words:
	if(words[key]>1):
		print ("no")
		exit()

print("yes")
