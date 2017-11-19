guess = 500
high = 1000
low = 1
answer = None

while answer!= 'correct':
	print(guess,flush=True)
	answer = input()
	if answer == 'higher':
		low = guess+1
		guess = int((high + low)/2)
	if answer == 'lower':
		high = guess-1
		guess = int((high + low)/2)

