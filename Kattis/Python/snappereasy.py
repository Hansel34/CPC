test_cases = int(input())

for i in range(test_cases):
    N, K = [int(x) for x in input().split()]
    K = str(bin(K))
    on = True
    for c in range(1,N+1):
        if (len(K)-2) < N:
            on = False
            continue
        if K[-c] == '0':
            on = False
    if on:
        print("Case #{}: ON".format(i+1))
    else:
        print("Case #{}: OFF".format(i+1))
            



