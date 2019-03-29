def f(n):
	while n > 1:
		return f(n-1)*n
	else:
		return n

for n in range(1,20):
	print ("{} {}".format(n,f(n)))