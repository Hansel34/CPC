L = int(input())
D = int(input())
X = int(input())

for i in range(L,D+1):
    if sum([int(c) for c in str(i)])== X:
        print(i)
        break
for i in range(D,L-1,-1):
    if sum([int(c) for c in str(i)])== X:
        print(i)
        break