totalwidth,totalinputs = [int(x) for x in input().split()]
inputs = [int(x) for x in input().split()] 
output = []
for x in range(totalinputs):
	for y in range(totalinputs):
		item = abs(inputs[y] - inputs[x])
		if item not in output:
			output.append(item)

for x in range(totalinputs):
	item = abs(totalwidth - inputs[x])
	if item not in output:
		output.append(item)

for x in range(totalinputs):
	item = (inputs[x] - 0)
	if item not in output:
			output.append(item)

output.append(totalwidth)

output.sort()

output.remove(0)

for x in output:
	print(x, end=' ')
