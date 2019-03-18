from sys import stdin
lines = stdin.readlines()

for line in lines:
    M , P, L, E, R, S, N = [int(x) for x in line.split()]
    eggs = 0
    for _ in range(N):
        M , P, L = P//S, L//R, M*E    
    print(M)

