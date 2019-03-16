while True:
    one,two,three,four = [int(x) for x in input().split()]
    if one == 0 and two == 0 and three == 0 and four == 0:
        break
    answer = 1080
    if two > one:
        one+=40
    answer+= (one - two) * 9
    if two > three:
        two-=40
    answer+= (three - two) * 9
    if four > three:
        three+=40
    answer+= (three - four) * 9

    print(answer)
