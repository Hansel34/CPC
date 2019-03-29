while True:
    w,l = [int(x) for x in input().split()]
    if w == 0 and l == 0:
        break
    n = int(input())
    robot_thinks = [0,0]
    actual = [0,0]
    for _ in range(n):
        move, distance = input().split()
        distance = int(distance)
        if move == 'r':
            robot_thinks[0]+=distance
            actual[0] = min(w-1,actual[0]+distance)
        if move == 'l':
            robot_thinks[0]-=distance
            actual[0] = max(0,actual[0]-distance)
        if move == 'u':
            robot_thinks[1]+=distance
            actual[1] = min(l-1,actual[1]+distance)
        if move == 'd':
            robot_thinks[1]-=distance
            actual[1] = max(0,actual[1]-distance)
    print("Robot thinks {} {}".format(robot_thinks[0],robot_thinks[1]))
    print("Actually at {} {}".format(actual[0],actual[1]))
    print()