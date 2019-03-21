values = [int(x) for x in input().split()]
values.sort()
output = [0]*3

for i,c in enumerate(input()):
    if c == 'A':
        output[i]=values[0]
    if c == 'B':
        output[i]=values[1]
    if c == 'C':
        output[i]=values[2]
print(" ".join([str(c) for c in output]))