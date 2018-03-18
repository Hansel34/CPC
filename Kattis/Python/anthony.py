import sys
sys.setrecursionlimit(3000)


def recursive(n, currN, currM):
    if currN == 0:
        return 0
    if currM == 0:
        return 1
    if memory[currN][n] > -1:
        return memory[currN][n]
    else:
        memory[currN][n] = probs[n]*recursive(n+1, currN, currM-1) + ((1-probs[n])*recursive(n+1, currN-1, currM)) 
        return memory[currN][n]

        


probs = []

N, M = map(int,raw_input().split())
memory = []
for x in range(1003):
    memory.append([])
    for y in range(2006):
        memory[x].append(-1)
orN = N
orM = M
for x in range(N+M-1):

    probs.append(float(input()))
    
print (str.format('{0:f}',(recursive(0,orN,orM))))