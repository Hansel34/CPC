A, B = [int(x) for x in input().split()]
M, O = [int(x) for x in input().split()]

if A >= B:
    y = 1
    x = M-1
    print(A*x+B*y)
else:
    if (O-M<=0):
        x =1
    else:
        x = O-M
    y = M-x
    print(A*x+B*y)