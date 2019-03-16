case = 1

while True:
    try:
        nums = [int(x) for x in input().split()][1:]
        min = float("inf")
        max = float("-inf")

        for num in nums:
            if num < min:
                min = num
            if num > max:
                max = num

        print("Case {}: {} {} {}".format(case,min,max,max-min))
        case+=1
    except EOFError:
        break