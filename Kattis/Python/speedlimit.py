while True:
    cases = int(input())
    if cases == -1:
        break
    start = 0
    miles = 0
    for _ in range(cases):
        speed, distance = [int(x) for x in input().split()]
        miles += (distance-start)*speed
        start = distance
    print(miles, "miles")