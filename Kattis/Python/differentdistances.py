while True:
    nums = [float(x) for x in input().split()]

    if len(nums) == 1:
        break
    
    print( (abs(nums[2]-nums[0])**nums[4] + abs(nums[3]-nums[1])**nums[4])**(1/nums[4]))