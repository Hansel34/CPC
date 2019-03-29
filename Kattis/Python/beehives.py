from math import hypot

while True:
    d, n = input().split()
    d, n = float(d), int(n)
    if d == 0 and n == 0:
        break
    positions = []
    for _ in range (n):
        positions.append([float(x) for x in input().split()])
    
    sour = 0

    for i in positions:
        for j in positions:
            if i == j:
                continue
            if hypot(i[0]-j[0],i[1]-j[1]) <= d:
                sour+=1
                break

    print("{} sour, {} sweet".format(sour,n-sour))

